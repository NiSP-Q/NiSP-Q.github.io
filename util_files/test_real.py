#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试真实文件的第一行
"""

from process_citations import parse_ieee_citation, classify_publication_type

# 读取真实文件的第一行
with open('publication/journal_paper.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline().strip()

print("测试真实文件的第一行")
print("=" * 50)
print(f"原文: {first_line}")

parsed = parse_ieee_citation(first_line)
if parsed['title']:
    parsed['tags'] = classify_publication_type(parsed)
    
    print(f"标题: {parsed['title']}")
    print(f"作者: {parsed['authors']}")
    print(f"期刊: {parsed['publisher']}")
    print(f"日期: {parsed['date']}")
    print(f"标签: {parsed['tags']}")
    print(f"ID: {parsed['id']}")
else:
    print("解析失败！")

print(f"\n测试完成！") 