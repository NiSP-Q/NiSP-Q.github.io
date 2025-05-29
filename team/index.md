---
title: Team
nav:
  order: 5
  tooltip: About our team
---



# <i class="fas fa-users"></i>Team
{% include section.html %} 

## Principal Investigator
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: professor"
%}

{% include section.html %}
## Postdoctoral Researcher
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}
## Graduate Students
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd_1"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd_2"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd_3"
%}

<hr style="margin: 2em 0;">
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: MASc_1"
%}
<!-- {%
  include list.html
  data="members"
  component="portrait"
  filters="role: MASc_2"
%} -->
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: MASc_3"
%}
{:.center}
{% include section.html %}

## Alumnus
{:.center}
<!-- {%
  include feature.html
  image="images/objectives.jpg"
  flip=true
  text=text
%} -->

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{% include section.html %}





