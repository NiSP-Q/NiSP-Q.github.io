---
title: Contact information
nav:
  order: 5
  tooltip: Email, address, and location
---

# <i class="fas fa-envelope"></i>Contact Information 

Our lab is part of the Department of Elctrical and computer engineering, at Queen's University.


{%
  include link.html
  type="email"
  icon=""
  text="jianbing.ni@queensu.ca"
  tooltip=""
  link="jianbing.ni@queensu.ca"
  style="button"
%}

{%
  include link.html
  type="address"
  icon=""
  text="Google Maps"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps/place/Walter+Light+Hall/@44.2279775,-76.4943801,17z/data=!3m2!4b1!5s0x4cd2ab03c9cc4e8f:0x8d5ec46a2b27023c!4m6!3m5!1s0x4cd2ab03c81307cb:0x568aa50f7fadb857!8m2!3d44.2279737!4d-76.4918052!16s%2Fg%2F11hcp7wps7?entry=ttu"
  style="button"
%}
{:.center}

{% include section.html %}

### <i class="fas fa-mail-bulk"></i>Mailing Address

Queen's University
19 Union St
Kingston, ON K7L 3N9
Canada
{:.center}

{% capture col1 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="The Center for Wit and Sagacity"
%}
{% endcapture %}
{% capture col2 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="Department of Metaphor"
%}
{% endcapture %}
{% include two-col.html col1=col1 col2=col2 %}
