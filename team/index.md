---
title: Team
nav:
  order: 5
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

{% include section.html %}
## Team
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: professor"
%}

## Current Team Members
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
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
{:.center}

{% include section.html %}

## Graduated Students
{:.center}
{%
  include feature.html
  image="images/objectives.jpg"
  flip=true
  text=text
%}

{% include section.html %}





