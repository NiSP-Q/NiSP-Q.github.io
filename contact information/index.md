---
title: Contact information
nav:
  order: 6
  tooltip: Email, address, and location
---

# <i class="fas fa-envelope"></i>Contact Information 

Our lab is part of the Department of Elctrical and computer engineering, at Queen's University. If you want to persue academic 


{%
  include link.html
  type="email"
  icon=""
  text="jianbing.ni@queensu.ca"
  tooltip=""
  link="jianbing.ni@queensu.ca"
  style="button"
%}
{:.center}
<!-- {%
  include link.html
  type="address"
  icon=""
  text="Google Maps"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps/place/Walter+Light+Hall/@44.2279775,-76.4943801,17z/data=!3m2!4b1!5s0x4cd2ab03c9cc4e8f:0x8d5ec46a2b27023c!4m6!3m5!1s0x4cd2ab03c81307cb:0x568aa50f7fadb857!8m2!3d44.2279737!4d-76.4918052!16s%2Fg%2F11hcp7wps7?entry=ttu"
  style="button"
%}
{:.center} -->


{% include section.html %}

<div class="container">
  <!-- Centered title -->
  <div class="text-center mb-4">
    <h3><i class="fas fa-map-marker-alt"></i> Our Location & Mailing Address</h3>
  </div>
  
  <!-- Use two-col component instead of Bootstrap grid -->
  {% capture col1 %}
  <p class="lead">
    <strong>Department of Electrical and Computer Engineering</strong><br>
    Walter Light Hall<br>
    Queen's University<br>
    Kingston, Ontario<br>
    Canada <br>
    K7L 3N6
  </p>
  {% endcapture %}
  
  {% capture col2 %}
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2858.9844994165633!2d-76.49438548766342!3d44.22797751494551!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cd2ab03c81307cb%3A0x568aa50f7fadb857!2sWalter%20Light%20Hall!5e0!3m2!1szh-CN!2sca!4v1746742355477!5m2!1szh-CN!2sca"
    width="100%" 
    height="350" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade"
    title="Location of Department of Electrical and Computer Engineering on map">
  </iframe>
  {% endcapture %}
  
  {% include two-col.html col1=col1 col2=col2 %}
</div>

<!-- <i class="fas fa-map-marker-alt"></i>Our Location & Mailing Address -->

<!-- <h3 style="text-align: center; margin-bottom: 20px;">
  <i class="fas fa-map-marker-alt"></i> Department of Electrical and Computer Engineering
</h3>




<div class="row flex s">
  <div class="col-xs-12 col-md-6">
    <p class="lead" style="margin-top: 0;">
      <strong>Department of Electrical and Computer Engineering</strong><br>
      Walter Light Hall<br>
      Queen's University<br>
      Kingston, Ontario<br>
      Canada <br>
      K7L 3N6
    </p>
  </div>


  <div class="col-xs-12 col-md-6">
    <iframe 
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2858.9844994165633!2d-76.49438548766342!3d44.22797751494551!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cd2ab03c81307cb%3A0x568aa50f7fadb857!2sWalter%20Light%20Hall!5e0!3m2!1szh-CN!2sca!4v1746742355477!5m2!1szh-CN!2sca"
      width="100%"   
      height="350" 
      style="border:0; display: block; margin: 0 auto;"
      allowfullscreen="" 
      loading="lazy" 
      referrerpolicy="no-referrer-when-downgrade"
      title="Location on map">
    </iframe>
    
  </div>
</div> -->


{% include section.html %}

<!-- ### <i class="fas fa-mail-bulk"></i>Mailing Address -->
<!-- 
Queen's University
19 Union St
Kingston, ON K7L 3N9
Canada
{:.center} -->

{% capture col1 %} 
{%
  include figure.html
  image="images/queens.jpg"
  caption="Queen's University"
  width="100%"
  height="400px"
%}
{% endcapture %} 
{% capture col2 %} 
{%
  include figure.html
  image="images/NISP.jpg"
  caption="NISP Lab"
  width="100%"
  height="400px"
%}
{% endcapture %}
{% include two-col.html col1=col1 col2=col2 %}
