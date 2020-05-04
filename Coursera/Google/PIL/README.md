<div class='js-lab-state' data-analytics-payload='{&quot;label&quot;:&quot;Scale and convert images using PIL&quot;,&quot;lab_name&quot;:&quot;Scale and convert images using PIL&quot;,&quot;classroom_name&quot;:null,&quot;deployment&quot;:&quot;googlecoursera-run&quot;}' data-focus-id='52111' data-lab-billing-limit='0.0' data-lab-duration='5400' data-parent='classroom'></div>
<ql-lab-control-panel class='js-lab-control-panel l-lab-control-panel' connectionDetails='[]' connectionFiles='[]' labControlButton='{&quot;disabled&quot;:false,&quot;pending&quot;:false,&quot;running&quot;:false}' labTimer='{&quot;ticking&quot;:false,&quot;secondsRemaining&quot;:5400}' studentResources='[]'></ql-lab-control-panel>
<div class='l-lab-main-body'>
<div class='js-lab-content lab-content'>
<div class='alert alert--fake js-alert'>
<p class='alert__message js-alert-message'></p>
</div>
<div class='lab-content__markdown-wrapper'>
<div class='lab-preamble'>
<h1 class='lab-preamble__title'>
Scale and convert images using PIL
</h1>
<div class='lab-preamble__details subtitle-headline-1'>
<span>1 hour 30 minutes</span>
<span>Free</span>
<div class='lab__rating'>
<a href="/focuses/52111/reviews?parent=catalog"><div class='rateit' data-rateit-readonly='true' data-rateit-value='4.2089'></div>

</a><a data-target='#lab-review-modal' data-toggle='modal'>
Rate Lab
</a>
</div>
</div>
</div>

<div class='lab-content__inner-wrapper'>
<div class='js-markdown-instructions lab-content__markdown markdown-lab-instructions' id='markdown-lab-instructions'>



<h2 id="step1">Introduction</h2>
<p>Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll need to use Python to get these images ready for launch.</p>
<h3>What you'll do</h3>
<p>Use the Python Imaging Library to do the following to a batch of images:</p>
<ul>
<li>Open an image</li>
<li>Rotate an image</li>
<li>Resize an image</li>
<li>Save an image in a specific format in a separate directory</li>
</ul>
<p>You'll have 90 minutes to complete this lab.</p>
<h2 id="step3">Download the file</h2>
<p>Your design contractor sent you the zipped file through his team drive. Download the file from the drive using the following CURL request:</p>
<pre><code>curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&amp;id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" &gt; /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&amp;confirm=`awk '/download/ {print $NF}' ./cookie`&amp;id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip &amp;&amp; sudo rm -rf cookie&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="5fe50f874fc9b1f9.png" src="https://cdn.qwiklabs.com/kj85%2Bf6VDnhdjRDmtzSiaU5D9vk8WNVJWiNeKKtWJ5U%3D"></p>
<p>List files using the command:</p>
<pre><code>ls&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="bfeaf6a7d282dcf5.png" src="https://cdn.qwiklabs.com/NW9Sum4yd4TkL7LXwNCw4lExYVhY6bEZ%2BFbknotqsnM%3D"></p>
<p>Unzip the file using the following command:</p>
<pre><code>unzip images.zip&#x000A;</code></pre>
<p>Navigate to the <code>images</code> folder using the following command:</p>
<pre><code>cd images&#x000A;</code></pre>
<p>To list images use the following command:</p>
<pre><code>ls&#x000A;</code></pre>
<p>The images received are in the wrong format:</p>
<ul>
<li>.tiff format</li>
<li>Image resolution 192x192 pixel (too large)</li>
<li>Rotated 90° anti-clockwise</li>
</ul>
<p>The images required for the launch should be in this format:</p>
<ul>
<li>
<p>.jpeg format</p>
</li>
<li>
<p>Image resolution 128x128 pixel</p>
</li>
<li>
<p>Should be straight</p>
</li>
</ul>
<h2 id="step4">Install Pillow</h2>
<p>We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python Imaging Library (PIL). Install <code>pillow</code> library using the following command:</p>
<pre><code>pip3 install pillow&#x000A;</code></pre>
<p>Python Imaging Library (known as Pillow in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats.</p>
<p>Pillow offers several standard procedures for image manipulation. These include:</p>
<ul>
<li>Per-pixel manipulations</li>
<li>Masking and transparency handling</li>
<li>Image filtering, such as blurring, contouring, smoothing, or edge finding</li>
<li>Image enhancing, like sharpening and adjusting brightness, contrast or color</li>
<li>Adding text to images (and much more!)</li>
</ul>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="1">
Install Pillow
</ql-activity-tracking></p>
<h2 id="step5">Write a Python script</h2>
<p>This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:</p>
<ul>
<li>Iterate through each file in the folder</li>
<li>For each file:
<ul>
<li>Rotate the image 90° clockwise</li>
<li>Resize the image from 192x192 to 128x128</li>
<li>Save the image to a new folder in .jpeg format</li>
</ul>
</li>
</ul>
<p>Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: <code>/opt/icons/</code></p>
<p>You'll use lots of  methods from PIL to complete this exercise. You can refer to  <a href="https://pillow.readthedocs.io/en/stable/reference/index.html">Pillow</a> for detailed explanations and have a look at the  <a href="https://pillow.readthedocs.io/en/stable/handbook/tutorial.html">tutorials</a> to help you build the script and complete the task.</p>
<p>To save the file after editing, press Ctrl-O, Enter, and Ctrl-x.</p>
<p>Once your script is ready, grant executable permission to the script file.</p>
<pre><code>chmod +x &lt;script_name&gt;.py&#x000A;</code></pre>
<p>Replace &lt;script_name&gt; with the name of your script.</p>
<p>Now, run the file.</p>
<pre><code>./&lt;script_name&gt;.py&#x000A;</code></pre>
<p>Replace &lt;script_name&gt; with the name of your script.</p>
<p>On a successful run, this should produce images in the right format within the directory: <code>/opt/icons/</code></p>
<p>To view the updated images use the following command:</p>
<pre><code>ls /opt/icons&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="ea9afeff1183c231.png" src="https://cdn.qwiklabs.com/nugr9eMy2HgOEUdhu%2B%2FjxldxZ4kh%2BeTDLLhwRD%2FGTsk%3D"></p>
<p>To check image properties, use the Python interpreter:</p>
<pre><code>python3&#x000A;</code></pre>
<p>Once the interactive shell opens, import the Image module from PIL:</p>
<pre><code>from PIL import Image&#x000A;</code></pre>
<p>Open any image from the folder, or you can use the following image:</p>
<pre><code>img = Image.open("/opt/icons/ic_edit_location_black_48dp")&#x000A;</code></pre>
<p>To view the format and size of the image:</p>
<pre><code>img.format, img.size&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="b3a2965a9c783ec9.png" src="https://cdn.qwiklabs.com/o1Bb%2Fm7Rt%2Fz3Vns5Ja3RUGD7%2BvgOW2%2FGN74SAL0fwcQ%3D"></p>
