---
title: Understanding the Right to be Forgotten and its Deployment
authors: 
  - name: Jianbing Ni
    member: miao
  - name: Xiangman Li
    member: xiangman
  - name: Eric Li
  - name: Jianxiang Zhao
---



# 1.Deployment of Services 

We conducted a sample study comprising 35 companies, categorized into 10 social platforms, 10 financial, 10 technical, and 4 government organizations. Based on this sample, we observed five distinct types of current implementation methods for data deletion: 1) deleting data via account setting, 2) using email communication, 3) submitting a written request, 
4) filling out an inquiry form, and 5) contacting customer support. The summary of these methods is presented in the following table.


{% capture content %}
{%
  include figure.html
  image="images/t1.jpg"
  caption="Social Media"
  width="600px"
%}
{%
  include figure.html
  image="images/t2.jpg"
  caption="Finance"
  width="600px"
%}
{%
  include figure.html
  image="images/t3.jpg"
  caption="Technical"
  width="600px"
%}
{%
  include figure.html
  image="images/t4.jpg"
  caption="Government"
  width="600px"
%}
{% endcapture %}

{%
  include grid.html
  content=content
  style="square"
%}

{% include section.html %}
{%
  include figure.html
  image="t6.jpg"
  caption="Types of implementation methods"
  width="600px"
%}

{%
  include figure.html
  image="images/t5.jpg"
  caption="Current Implementation Methods"
  width="400px"
%}

{% include section.html %}
## Conclusion
From the table above, it is evident that the "Account Setting" method is the most widely used approach for users to exercise their 
data deletion right (right to be forgotten), and this method is adopted by most social media companies. However, all governmental 
organizations do not make any statement or provide a way for users to request the deletion of their data.  

Regarding the rights to erasure in Discord, besides offering a way to delete data by deleting the account, it also provides an 
automated scheme wherein users' data would be deleted if their accounts remain inactive for more than two years. This data deletion 
scheme is commendable as it fulfills the right of erasure without requiring users to submit deletion requests themselves. In other 
words, for those concerned about their data privacy, they need not worry about whether their data will be deleted, even 
if they have not actively requested it.  

On the other hand, it is observed that all governmental agencies do not provide a way for users to request data deletion. The reason behind this is that most of the data processed by the government is done as a result of legal obligations or to carry out public tasks, and users cannot request the deletion of this data.



{% include section.html %}
{%
  include button.html
  type="github"
  link="/erasure/eresult.html"
  icon="fa-solid fa-arrow-left"
  text="Back to Project Page"
  tooltip="Back to Project Page"
  flip=true
  style="bare"
%}
