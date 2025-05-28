#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试所有引用处理（禁用网络搜索）
"""

from process_citations import process_citation_file

print("快速测试引用处理（禁用网络搜索）")
print("=" * 50)

# 处理期刊论文（禁用网络搜索）
print("\n处理期刊论文...")
if process_citation_file('publication/journal_paper.txt', 'journal_citations_test.yaml', enable_web_search=False):
    print("✓ 期刊论文处理完成")
else:
    print("✗ 期刊论文处理失败")

# 处理会议论文（禁用网络搜索）
print("\n处理会议论文...")
if process_citation_file('publication/conference_paper.txt', 'conference_citations_test.yaml', enable_web_search=False):
    print("✓ 会议论文处理完成")
else:
    print("✗ 会议论文处理失败")

print("\n快速测试完成！") 