#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试IEEE引用解析功能
"""

from process_citations import parse_ieee_citation, classify_publication_type

# 测试几个样例
test_citations = [
    'M. R. Jabari*, J. Ni, N. Lu, S. S.-H. Yam, and F. Chan, "An Evolutionary Approach for Multiple Flying Base Stations Deployment in NOMA-based Networks," IEEE Transactions on Vehicular Technology, to appear.',
    'J. Zhou, J. Wu, J. Ni, Y. Wang, Y. Pan, and Z. Su, "Protecting Your Attention during Distributed Graph Learning: Privacy-preserving Federated Graph Attention Network," IEEE Transactions on Information Forensics & Security, to appear.',
    'X. Wu*, X. Li*, J. Ni, and R. Lu, "Evaluating Security and Robustness for Split Federated Learning against Poisoning," IEEE Transactions on Information Forensics & Security, vol. 20, pp. 175-190, 2025.'
]

print("测试IEEE引用解析功能")
print("=" * 50)

for i, citation in enumerate(test_citations, 1):
    print(f"\n测试 {i}:")
    print(f"原文: {citation}")
    
    parsed = parse_ieee_citation(citation)
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