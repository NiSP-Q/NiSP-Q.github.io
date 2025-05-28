#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IEEE引用格式转换脚本（增强版）
将IEEE格式的引用转换为lab-website-template所需的sources.yaml格式
包含自动DOI查找和Google Scholar搜索功能
"""

import re
import yaml
from datetime import datetime
import sys
import requests
import time
import urllib.parse
from bs4 import BeautifulSoup
import json

# 配置
DELAY_BETWEEN_REQUESTS = 2  # 请求间隔（秒）
MAX_RETRIES = 3  # 最大重试次数

def search_crossref_doi(title, authors=None, year=None):
    """使用Crossref API搜索DOI"""
    try:
        # 构建查询参数
        query_parts = [title]
        if authors and len(authors) > 0:
            # 取第一个作者的姓氏
            first_author = authors[0].split()[-1] if authors[0] else ""
            if first_author:
                query_parts.append(first_author)
        
        query = " ".join(query_parts)
        
        # Crossref API URL
        url = "https://api.crossref.org/works"
        params = {
            'query': query,
            'rows': 5,  # 返回前5个结果
            'sort': 'relevance'
        }
        
        if year:
            params['filter'] = f'from-pub-date:{year},until-pub-date:{year}'
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Academic Research Tool; mailto:your@email.com)'
        }
        
        print(f"    搜索DOI: {query[:50]}...")
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('message', {}).get('items', [])
            
            for item in items:
                result_title = item.get('title', [''])[0].lower()
                search_title = title.lower()
                
                # 简单的标题匹配
                if len(result_title) > 10 and len(search_title) > 10:
                    # 计算标题相似度（简单的词汇重叠）
                    title_words = set(search_title.split())
                    result_words = set(result_title.split())
                    overlap = len(title_words & result_words) / len(title_words | result_words)
                    
                    if overlap > 0.5:  # 50%以上的词汇重叠
                        doi = item.get('DOI')
                        if doi:
                            print(f"    ✓ 找到DOI: {doi}")
                            return f"doi:{doi}"
        
        print("    ✗ 未找到匹配的DOI")
        return None
        
    except Exception as e:
        print(f"    ✗ DOI搜索失败: {str(e)}")
        return None

def search_google_scholar(title, authors=None):
    """搜索Google Scholar链接"""
    try:
        # 构建搜索查询
        query = f'"{title}"'
        if authors and len(authors) > 0:
            first_author = authors[0].split()[-1] if authors[0] else ""
            if first_author:
                query += f" {first_author}"
        
        # Google Scholar搜索URL
        encoded_query = urllib.parse.quote(query)
        url = f"https://scholar.google.com/scholar?q={encoded_query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"    搜索Google Scholar: {title[:50]}...")
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 查找第一个搜索结果
            results = soup.find_all('div', class_='gs_r gs_or gs_scl')
            if not results:
                results = soup.find_all('div', class_='gs_ri')
            
            if results:
                first_result = results[0]
                title_link = first_result.find('a')
                if title_link and title_link.get('href'):
                    link = title_link.get('href')
                    if link.startswith('/'):
                        link = 'https://scholar.google.com' + link
                    print(f"    ✓ 找到Google Scholar链接")
                    return link
        
        print("    ✗ 未找到Google Scholar链接")
        return None
        
    except Exception as e:
        print(f"    ✗ Google Scholar搜索失败: {str(e)}")
        return None

def search_ieee_xplore(title, authors=None):
    """搜索IEEE Xplore链接"""
    try:
        # 简单的IEEE Xplore搜索
        query = title.replace('"', '').replace("'", "")
        encoded_query = urllib.parse.quote(query)
        url = f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={encoded_query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        print(f"    搜索IEEE Xplore: {title[:50]}...")
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 查找搜索结果链接
            result_links = soup.find_all('a', href=re.compile(r'/document/\d+'))
            if result_links:
                first_link = result_links[0].get('href')
                if first_link.startswith('/'):
                    full_link = 'https://ieeexplore.ieee.org' + first_link
                    print(f"    ✓ 找到IEEE Xplore链接")
                    return full_link
        
        print("    ✗ 未找到IEEE Xplore链接")
        return None
        
    except Exception as e:
        print(f"    ✗ IEEE Xplore搜索失败: {str(e)}")
        return None

def enhance_citation_with_web_search(citation):
    """使用网络搜索增强引用信息"""
    enhanced = citation.copy()
    
    title = citation.get('title', '')
    authors = citation.get('authors', [])
    publisher = citation.get('publisher', '')
    
    # 提取年份用于DOI搜索
    year = None
    date_str = citation.get('date', '')
    if date_str:
        year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
        if year_match:
            year = year_match.group(0)
    
    if not title:
        print("    跳过：没有标题")
        return enhanced
    
    print(f"\n正在增强引用: {title[:60]}...")
    
    # 搜索DOI
    if not enhanced.get('id') or enhanced.get('id', '').startswith('temp:'):
        doi = search_crossref_doi(title, authors, year)
        if doi:
            enhanced['id'] = doi
        time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # 初始化extra-links
    if 'extra-links' not in enhanced:
        enhanced['extra-links'] = []
    
    # 搜索Google Scholar链接
    scholar_link = search_google_scholar(title, authors)
    if scholar_link:
        enhanced['extra-links'].append({
            'type': 'google-scholar',
            'link': scholar_link,
            'text': 'Google Scholar'
        })
    time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # 如果是IEEE论文，搜索IEEE Xplore链接
    if 'ieee' in publisher.lower():
        ieee_link = search_ieee_xplore(title, authors)
        if ieee_link:
            enhanced['extra-links'].append({
                'type': 'ieee',
                'link': ieee_link,
                'text': 'IEEE Xplore'
            })
        time.sleep(DELAY_BETWEEN_REQUESTS)
    
    return enhanced

def parse_ieee_citation(citation_text):
    """解析IEEE格式的引用"""
    citation_text = citation_text.strip()
    
    # 初始化结果字典
    result = {
        'id': '',
        'title': '',
        'authors': [],
        'publisher': '',
        'date': '',
        'tags': []
    }
    
    # 提取标题（用引号包围的部分，支持Unicode智能引号）
    title_match = re.search(r'["\u201C\u201D]([^"\u201C\u201D]+)["\u201C\u201D]', citation_text)
    if title_match:
        result['title'] = title_match.group(1).strip().rstrip(',')  # 移除末尾逗号
    else:
        # 如果没有找到引号，可能格式有问题
        print(f"    警告：未找到标题引号: {citation_text[:100]}...")
        return result
    
    # 提取作者（引号前的部分）
    if title_match:
        authors_part = citation_text[:title_match.start()].strip().rstrip(',')
        # 分割作者并清理
        if authors_part:
            authors = [author.strip() for author in authors_part.split(',')]
            # 清理作者名字中的特殊字符
            cleaned_authors = []
            for author in authors:
                # 移除 * 标记和多余的空格
                author = re.sub(r'\*', '', author)
                author = re.sub(r'\s+', ' ', author).strip()
                if author and len(author) > 1:  # 过滤掉空字符串和单字符
                    cleaned_authors.append(author)
            result['authors'] = cleaned_authors
    
    # 提取期刊/会议名称和其他信息（引号后的部分）
    if title_match:
        remainder = citation_text[title_match.end():].strip().lstrip(',').strip()
        
        # 尝试提取年份
        year_matches = re.findall(r'\b(19\d{2}|20\d{2})\b', remainder)
        if year_matches:
            # 取最后一个年份（通常是发表年份）
            year = year_matches[-1]
            result['date'] = f"{year}-01-01"
        else:
            # 如果没有找到年份，检查是否有"to appear"
            if 'to appear' in remainder.lower():
                result['date'] = "2024-01-01"  # 默认为即将发表
        
        # 提取期刊/会议名称
        # 移除卷号、页码等信息，保留期刊/会议名称
        publisher_part = remainder
        
        # 清理各种格式的卷号、页码信息
        publisher_part = re.sub(r',\s*vol\.\s*\d+.*$', '', publisher_part, flags=re.IGNORECASE)
        publisher_part = re.sub(r',\s*pp\.\s*[\d\-–—]+.*$', '', publisher_part, flags=re.IGNORECASE)
        publisher_part = re.sub(r',\s*no\.\s*\d+.*$', '', publisher_part, flags=re.IGNORECASE)
        publisher_part = re.sub(r',\s*\d{4}.*$', '', publisher_part)  # 移除年份及之后的内容
        publisher_part = re.sub(r',\s*to appear.*$', '', publisher_part, flags=re.IGNORECASE)
        publisher_part = re.sub(r'\s*\([^)]*\)\s*$', '', publisher_part)  # 移除末尾的括号内容
        
        # 进一步清理
        publisher_part = publisher_part.strip().rstrip(',').strip()
        
        if publisher_part:
            result['publisher'] = publisher_part
    
    # 生成临时ID（基于标题的简化版本）
    if result['title']:
        # 创建一个基于标题的简单ID
        title_words = re.sub(r'[^\w\s]', '', result['title'].lower()).split()
        title_id = '_'.join(title_words[:5])  # 取前5个单词
        result['id'] = f"temp:{title_id}"
    
    return result

def classify_publication_type(citation):
    """根据期刊/会议名称分类文献类型"""
    publisher = citation.get('publisher', '').lower()
    title = citation.get('title', '').lower()
    
    # 网络安全相关标签
    security_keywords = ['security', 'privacy', 'authentication', 'encryption', 'blockchain', 'secure']
    # 通信相关标签
    communication_keywords = ['wireless', 'communication', 'network', 'vehicular', 'mobile']
    # 机器学习相关标签
    ml_keywords = ['learning', 'neural', 'federated', 'ai', 'intelligence']
    # 物联网相关标签
    iot_keywords = ['iot', 'internet of things', 'edge', 'cloud']
    
    tags = []
    
    # 根据期刊/会议名称添加标签
    if 'ieee' in publisher:
        tags.append('IEEE')
    
    if any(keyword in publisher or keyword in title for keyword in security_keywords):
        tags.append('security')
    
    if any(keyword in publisher or keyword in title for keyword in communication_keywords):
        tags.append('communications')
        
    if any(keyword in publisher or keyword in title for keyword in ml_keywords):
        tags.append('machine learning')
        
    if any(keyword in publisher or keyword in title for keyword in iot_keywords):
        tags.append('IoT')
    
    # 根据期刊类型添加标签
    if 'transaction' in publisher:
        tags.append('journal')
    elif 'conference' in publisher or 'proc.' in publisher:
        tags.append('conference')
        
    return tags

def process_citation_file(input_file, output_file, enable_web_search=True):
    """处理引用文件"""
    citations = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 修复：每行都是一个独立的引用
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if line:  # 非空行
                print(f"处理第 {line_num} 行引用...")
                parsed = parse_ieee_citation(line)
                if parsed['title']:  # 只处理有标题的引用
                    # 添加分类标签
                    parsed['tags'] = classify_publication_type(parsed)
                    citations.append(parsed)
                    print(f"  ✓ 成功解析: {parsed['title'][:50]}...")
                else:
                    print(f"  ✗ 解析失败: {line[:50]}...")
    
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
        return False
    except Exception as e:
        print(f"处理文件时出错：{e}")
        return False
    
    print(f"共解析出 {len(citations)} 条有效引用")
    
    # 使用网络搜索增强引用信息
    if enable_web_search and citations:
        print(f"\n开始网络搜索增强 {len(citations)} 条引用...")
        print("=" * 50)
        
        enhanced_citations = []
        for i, citation in enumerate(citations, 1):
            print(f"\n[{i}/{len(citations)}]", end=" ")
            try:
                enhanced = enhance_citation_with_web_search(citation)
                enhanced_citations.append(enhanced)
            except Exception as e:
                print(f"    处理失败: {str(e)}")
                enhanced_citations.append(citation)
        
        citations = enhanced_citations
        print(f"\n网络搜索完成！")
    
    # 转换为YAML格式并保存
    try:
        # 写入YAML文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# 请将此内容添加到 _data/sources.yaml 文件中\n")
            f.write("# 然后运行: python auto-cite/auto-cite.py 生成最终引用\n\n")
            
            for citation in citations:
                # 写入基本信息
                if citation['id'] and not citation['id'].startswith('temp:'):
                    f.write(f"- id: {citation['id']}\n")
                else:
                    f.write("- id: # TODO: 添加DOI\n")
                
                # 写入日期（简化格式）
                if citation['date']:
                    # 转换为简化日期格式 (YYYY-M-D)
                    date_parts = citation['date'].split('-')
                    if len(date_parts) == 3 and date_parts[1] == '01' and date_parts[2] == '01':
                        simplified_date = date_parts[0]  # 只保留年份
                    else:
                        simplified_date = citation['date']
                    f.write(f"  date: {simplified_date}\n")
                
                # 写入图片（如果有的话）
                f.write("  # image: # 添加论文相关图片URL\n")
                
                # 写入仓库（如果有的话）
                f.write("  # repo: # 添加GitHub仓库链接\n")
                
                # 写入链接
                if citation.get('extra-links'):
                    f.write("  extra-links:\n")
                    for link in citation['extra-links']:
                        f.write(f"    - type: {link['type']}\n")
                        f.write(f"      link: {link['link']}\n")
                        if link.get('text'):
                            f.write(f"      text: {link['text']}\n")
                
                # 写入标签
                if citation.get('tags'):
                    f.write("  tags:\n")
                    for tag in citation['tags']:
                        f.write(f"    - {tag}\n")
                
                # 添加注释信息（便于识别）
                f.write(f"  # 标题: {citation.get('title', 'N/A')}\n")
                f.write(f"  # 作者: {', '.join(citation.get('authors', []))}\n")
                f.write(f"  # 期刊: {citation.get('publisher', 'N/A')}\n")
                
                f.write("\n")
        
        print(f"成功处理 {len(citations)} 条引用")
        print(f"结果已保存到 {output_file}")
        
        # 统计网络搜索结果
        doi_found = sum(1 for c in citations if c.get('id') and not c.get('id', '').startswith('temp:'))
        scholar_found = sum(1 for c in citations if c.get('extra-links') and 
                           any(link.get('type') == 'google-scholar' for link in c.get('extra-links', [])))
        
        print(f"\n网络搜索统计:")
        print(f"- 找到DOI: {doi_found}/{len(citations)}")
        print(f"- 找到Google Scholar链接: {scholar_found}/{len(citations)}")
        
        print("\n请注意：")
        print("1. 请验证自动找到的DOI是否正确")
        print("2. 将内容复制到 _data/sources.yaml 文件")
        print("3. 可以添加论文相关的图片URL和GitHub仓库链接")
        print("4. 运行 python auto-cite/auto-cite.py 生成最终的citations.yaml")
        
        return True
        
    except Exception as e:
        print(f"保存文件时出错：{e}")
        return False

def main():
    """主函数"""
    print("IEEE引用格式转换工具（增强版）")
    print("包含自动DOI查找和Google Scholar搜索")
    print("=" * 60)
    
    # 询问是否启用网络搜索
    enable_search = input("\n是否启用网络搜索功能？(y/N): ").lower().strip()
    enable_web_search = enable_search in ['y', 'yes', '是']
    
    if enable_web_search:
        print("✓ 网络搜索已启用")
        print("注意：这可能需要几分钟时间，请耐心等待...")
    else:
        print("✗ 网络搜索已禁用")
    
    # 处理期刊论文
    print("\n处理期刊论文...")
    if process_citation_file('publication/journal_paper.txt', 'journal_citations.yaml', enable_web_search):
        print("✓ 期刊论文处理完成")
    else:
        print("✗ 期刊论文处理失败")
    
    # 处理会议论文
    print("\n处理会议论文...")
    if process_citation_file('publication/conference_paper.txt', 'conference_citations.yaml', enable_web_search):
        print("✓ 会议论文处理完成")
    else:
        print("✗ 会议论文处理失败")
    
    print("\n处理完成！")
    print("\n下一步：")
    print("1. 检查生成的YAML文件")
    print("2. 验证自动找到的DOI和链接")
    print("3. 手动添加缺失的信息")
    print("4. 将内容合并到 _data/sources.yaml")
    print("5. 运行 python auto-cite/auto-cite.py 生成最终引用")

if __name__ == "__main__":
    main() 