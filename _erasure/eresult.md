---
title: Right to be erasure
authors: 
  - name: Jianbing Ni
    member: miao
  - name: Xiangman Li
    member: xiangman
  - name: Eric Li
  - name: Jianxiang Zhao
---


# Background

The ubiquitous data collection poses severe risks of privacy leakage to customers who access
various web services in the connected world. Due to the frequently occurred data breach
incidents, the regulation of data collection and usage has been attracting much attention, and
various privacy laws have been issued to promote personal data protection. To ensure the closure
of data lifecycle, data deletion is critical but always neglected. The GDPR Article 17 [1](https://gdpr-info.eu/)
introduces a right to erasure (also called right to be forgotten), in which the data subject (i.e.,
customer) shall have the right to erase the personal data held by the service providers (e.g.,
government, tech giants, or research institutions) without undue delay. However, the right to
erasure is hard to be regulated. The service providers maintain the personal data without
exposing the real storage address. Even the customers ask for data deletion, it is challenging to
know whether the service provider deletes the data indeed. The service providers may refuse to
delete the customer’s data on their servers or on the cloud due to monetary benefits; after all,
some data has high value. The service providers are not motivated to delete the data, although the
right to erasure allows the customers who concern the leakage of their uncontrollable personal
data to submit data deletion requests. What is worse, there is no effective approach to tracing the
personal data or verifying the execution of data deletion. The difficulty of regulation might be
one of the reasons that the PIPEDA [2](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/page-7.html) does not grant Canadians the right to be forgotten. In this
project, we aim to understand real needs of customers on the right to erasure and design solutions
to achieve secure personal data deletion with public verifiability.

For more detail, please refer to our technical report [Understanding the Right to be Forgotten and its Deployment](OPC Contribution.pdf).



{% include section.html %}
# Our Objectives

{% capture text %}
•	We propose a study on the right of erasure in current privacy laws, including Canada's PIPEDA and CPPA, EU's GDPR, US's ECPA and CCPA, 
China's PIPL, Japan’s APPI, and UK's DPA, comparing the differences in statements about personal information, right to be informed, right of access, 
right of modification, and right to erasure in these privacy laws.  

•	We introduce the implementation methods of the right of erasure on 35 platforms, including WhatsApp, LinkedIn, Twitter, Meta, Manulife, 
Bell, Apple, etc., and summarize the existing methods: account setting, written request, email, inquiry form, 
contact the IT team, or mixed.  

•	We design an online survey about the right to be forgotten and proof of erasure, comprising 18 
questions to collect knowledge from the general public regarding data deletion policies they seek and their concerns about 
personal data management policies of government, tech giants, and research institutions.  

•	We present the survey results, which demonstrate the general public's concerns about privacy leakage, 
their understanding of privacy policies, their usage of data deletion methods, their need for the right to be forgotten, 
and their recognition of the importance of proof of erasure.  
{% endcapture %}

{%
  include feature.html
  image="images/objectives.jpg"
  flip=true
  text=text
%}



{% include section.html %}
# Deployment Methods

We collected the privacy policy statements and the deployed methods of the right to be forgotten on 35 platforms, grouped based on their services. The methods identified are as follows:  

•	Account Setting: The user can delete the account on systems or apps.  
•	Email: The user needs to send emails to the companies or organizations to request the deletion of personal information.  
•	Written request: The user needs to write a request and mail it to the companies or organizations to request the deletion of
 personal information.  
•	Inquiry form: The user needs to fill in an inquiry form and submit it to 
the companies or organizations to request the deletion of personal information.  
•	Contact us: The user needs to call customer support of the companies or organizations to
 request the deletion of personal information.  
 
The conditions for data deletion include:  
•	The number of days that the personal information will be kept on the servers after the request has been received.  
•	The laws and guidelines for companies or institutions on the management of personal information. 
•	The needs of the companies or organizations regarding personal information for managing products and services.  

Our detailed findings and insights are compiled in [this report](Depresult.html), which presents an in-depth review of our analyses.




{% include section.html %}
# Discovery Private law in different countries and Areas
{% capture text %}
In 2016, the European Parliament approved the General Data Protection Regulation (GDPR), which was implemented on May 25th, 2018. 
This regulation brought about a notable overhaul compared to its predecessor, incorporating a stricter approach to penalizing non-compliance. [1](https://gdpr-info.eu/)  
{% endcapture %}

{%
  include feature.html
  image="images/gdpr.jpg"
  title="GDPR"
  text=text
%}



{% capture text %}
The Personal Information Protection and Electronic Documents Act (PIPEDA) is the federal privacy law for private-sector organizations.
It sets out the ground rules for how businesses must handle personal information in the course of their commercial activity. [2](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/page-7.html)
{% endcapture %}

{%
  include feature.html
  image="images/pipeda.jpg"
  title="PIPEDA"
  text=text
%}



{% capture text %}
The Digital Charter Implementation Act (Bill C-11) introduces new regulations governing the collection, sharing, and utilization of data. 
The Consumer Privacy Protection Act (CPPA) has been included as part of Bill C-11. [3](https://www.parl.ca/DocumentViewer/en/44-1/bill/C-27/first-reading#:~:text=Part%201%20enacts%20the%20Consumer,the%20course%20of%20commercial%20activities)
{% endcapture %}

{%
  include feature.html
  image="images/cppa.jpg"
  title="CPPA"
  text=text
%}


{% capture text %}
The Electronic Communications Privacy Act (ECPA) of 1986, encompassing both the Electronic Communications Privacy Act 
and the Stored Wire Electronic Communications Act, has been subject to subsequent legislative amendments, such as the USA PATRIOT Act. [4](https://bja.ojp.gov/program/it/privacy-civil-liberties/authorities/statutes/1285#:~:text=General%20Provisions,conversations%2C%20and%20data%20stored%20electronically)
{% endcapture %}

{%
  include feature.html
  image="images/ecpa.jpg"
  title="ECPA"
  text=text
%}



{% capture text %}
The CCPA is considered the most comprehensive data protection regulation in the United States, introducing significant 
reforms similar to those seen in the GDPR. While both laws share the common goal of effectively safeguarding consumers' personal data, 
they do exhibit notable differences in their approach and provisions. [5](https://oag.ca.gov/privacy/ccpa#:~:text=The%20CCPA%20requires%20business%20privacy,the%20Right%20to%20Non%2DDiscrimination)
{% endcapture %}

{%
  include feature.html
  image="images/ccpa.jpg"
  title="CCPA"
  text=text
%}


{% capture text %}
On August 20th, 2021, China formally adopted the Personal Information Protection Law (PIPL). 
PIPL  focusing on safeguarding personal information of individuals and establishing comprehensive protections for data privacy.[6](https://digichina.stanford.edu/work/translation-personal-information-protection-law-of-the-peoples-republic-of-china-effective-nov-1-2021/)
{% endcapture %}

{%
  include feature.html
  image="images/pipl.jpg"
  title="PIPL"
  text=text
%}



{% capture text %}
Japan implemented the Act on the Protection of Personal Information (APPI) in 2003, making it one of the pioneering legislations in Asia and worldwide. [7](https://elaws.e-gov.go.jp/document?lawid=415AC0000000057)
{% endcapture %}

{%
  include feature.html
  image="images/appi.jpg"
  title="APPI"
  text=text
%}


{% capture text %}
On May 23，2018, the UK officially enacted the revised Data Protection Act 2018. 
The new act aims to support the effective implementation of the GDPR within the UK while suit the country's requirements. [8](https://www.legislation.gov.uk/ukpga/2018/12/contents/enacted)
{% endcapture %}

{%
  include feature.html
  image="images/dpa.jpg"
  title="DPA"
  text=text
%}

We also studied Right to be Forgotten in Privacy Acts. Our detailed findings and insights are compiled in [this report](sresult.html), which presents an in-depth review of our analyses.



{% include section.html %}
# Data Security and Privacy Survey: Knowledge on the Right to be Forgotten.

We are in the process of administering [this survey](https://www.surveymonkey.com/r/F77JPSQ) which aims to explore the level of public understanding regarding their rights to online data deletion.
This encapsulates the extent to which the general populace realizes they can demand companies or institutions to erase their personal data - be it account-related details or data acquired from online activities.
Our research also investigates the existing procedures implemented to exercise data deletion rights across different data platforms,
like the option for account deletion or the provision to submit requests through email or written forms.
The final goal of our study is to discern the public's preferred policies for deleting personal online data.  

Following the completion of our survey, we received 2000 responses, which we have meticulously analyzed and compiled into a 
comprehensive research report.   
Our detailed findings and insights are compiled in [this report](survey.html), which presents an in-depth review of our analyses.

   
{% include section.html %}
# Our Research

{% capture text %}
Our research is [Accelerating Secure and Verifiable Data Deletion in Cloud Storage via SGX and Blockchain](https://arxiv.org/abs/2307.04316)
In this study, we introduce SevDel, a robust data deletion mechanism that ensures both security and verifiability. 
This system capitalizes on zero-knowledge proof to verify the encryption of outsourced data without necessitating the retrieval of ciphertexts, 
while the deletion of encryption keys is safeguarded through Intel SGX. 
SevDel equips a secure cloud storage environment with interfaces specifically designed to perform data encryption and decryption. 
Moreover, it employs a smart contract to ensure that the cloud service provider's operations align with the service level agreements made with data owners,
including potential penalties if the provider improperly discloses data stored on their servers. Evaluations conducted on real-world workloads 
show that SevDel not only efficiently verifies data deletion but also significantly enhances bandwidth savings.
{% endcapture %}

{%
  include feature.html
  image="images/research.png"
  flip=true
  text=text
%}

{% include section.html %}
#### Acknowledgement
This project is supported by the Office of the Privacy Commissioner of Canada (OPC) Contributions Program 2022-2023