<h1 class='lab-preamble__title'>
Process Text Files with Python Dictionaries and Upload to Running Web Service
</h1>
<div class='lab-preamble__details subtitle-headline-1'>
<span>1 hour 30 minutes</span>
<span>Free</span>
</div>
</div>
</div>

<div class='lab-content__inner-wrapper'>
<div class='js-markdown-instructions lab-content__markdown markdown-lab-instructions' id='markdown-lab-instructions'>



<h2 id="step1">Introduction</h2>
<p>You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company's website (currently using Django).</p>
<h3>What you'll do</h3>
<ul>
<li>Use the Python OS module to process a directory of text files</li>
<li>Manage information stored in Python dictionaries</li>
<li>Use the Python requests module to upload content to a running Web service</li>
<li>Understand basic operations for Python requests like GET and POST methods</li>
</ul>
<p>You'll have 90 minutes to complete this lab.</p>
<h2 id="step3">Web server corpweb</h2>
<p><strong>Django</strong> is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. A Web framework is a set of components that provide a standard way to develop websites quickly and easily.</p>
<p>For this lab, a Django web server <code>corpweb</code> is already configured under <code>/projects/corpweb</code> directory. You can check it out by visiting the external IP address of the <code>corpweb</code> VM. The external IP address can be found in the connection details panel. Enter the <code>corpweb</code> external IP address in a new separate browser tab.</p>
<p>Output:</p>
<p><img alt="6d4dcdc788626521.png" src="https://cdn.qwiklabs.com/oTBchVUq807yFZsqyMsAfEt%2F2T9McWLGQ39BWNH4lFI%3D"></p>
<p>You'll see that there's currently no feedback.</p>
<p>Now, append <code>/feedback</code> to the external IP address of <code>corpweb</code> VM opened in the browser tab.</p>
<p><img alt="4c82e605dae520f3.png" src="https://cdn.qwiklabs.com/irg5MZwCPQdQQZPVXYKwLR5rlg2VJ%2FZsOr8mFmc0nEs%3D"></p>
<p>This is a web interface for a REST end-point. Through this end-point, you can enter feedback that can be displayed on the company's website. You can use this end-point in the example below. Start by copying and pasting the following JSON to the <strong>Content</strong> field on the website, and click <strong>POST</strong>.</p>
<pre><code>{"title": "Experienced salespeople", "name": "Alex H.", "date": "2020-02-02", "feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}&#x000A;</code></pre>
<p>Now, go back to the main page by removing the <code>/feedback</code> from the URL. You can see that the feedback that you just entered is displayed on the webpage.</p>
<p><img alt="971893c6631c06f6.png" src="https://cdn.qwiklabs.com/sYBz1LWL83hyw7D2NrCBo51J6WGO5DSpdZf0Ix1a3Ms%3D"></p>
<p>The whole website is stored in <code>/projects/corpweb</code>. You're free to look around the configuration files. Also, there's no need to make any changes to the website; all interaction should be done through the REST end-point.</p>
<h2 id="step4">Process text files and upload to running web server</h2>
<p>In this section, you'll write a Python script that will upload the feedback automatically without having to turn it into a dictionary.</p>
<p>Navigate to <code>/data/feedback</code> directory, where you'll find a few .txt files with customer reviews for the company.</p>
<pre><code>cd /data/feedback&#x000A;</code></pre>
<pre><code>ls&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="80676af4c8e69cc4.png" src="https://cdn.qwiklabs.com/%2B3MkEuvftlNNBZUs7YVVPPgta0D6uo4RpebSSDEC4d8%3D"></p>
<p>Use the <code>cat</code> command to view these files.  For example:</p>
<pre><code>cat 007.txt&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="336fe102a3cdc30b.png" src="https://cdn.qwiklabs.com/iqjatGUkTc7ZHbJrF62dI9e%2B%2F5Cavugl5CHPktDfn28%3D"></p>
<p>They're all written in the same format (i.e. <code>title, name, date,</code> and <code>feedback).</code></p>
<p>Here comes the challenge section of the lab, where you'll write a Python script that uploads all the feedback stored in this folder to the company's website, without having to turn it into a dictionary one by one.</p>
<p>Now, navigate back to the <code>home</code> directory and create a Python script named <code>run.py</code> using the following command:</p>
<pre><code>cd ~&#x000A;</code></pre>
<pre><code>nano run.py&#x000A;</code></pre>
<p>Add the shebang line:</p>
<pre><code>#! /usr/bin/env python3&#x000A;</code></pre>
<p>The following are a few libraries that will be required for the script. Import them using:</p>
<pre><code>import os&#x000A;import requests&#x000A;</code></pre>
<p>The script should now follow the structure:</p>
<ul>
<li>
<p>List all .txt files under <code>/data/feedback</code> directory that contains the actual feedback to be displayed on the company's website.</p>
<ql-infobox><strong>Hint:</strong> Use os.listdir() method for this, which returns a list of all files and directories in the specified path.</ql-infobox>
</li>
<li>
<p>You should now have a list that contains all of the feedback files from the path <code>/data/feedback</code>. Traverse over each file and, from the contents of these text files, create a dictionary by keeping <code>title</code>, <code>name</code>, <code>date</code>, and <code>feedback</code> as keys for the content value, respectively.</p>
</li>
<li>
<p>Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.</p>
</li>
<li>
<p>Use the Python <code>requests</code> module to post the dictionary to the company's website. Use the request.post() method to make a POST request to <code>http://&lt;corpweb-external-IP&gt;/feedback</code>. Replace <code>&lt;corpweb-external-IP&gt;</code> with corpweb's external IP address.</p>
</li>
<li>
<p>Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response <code>status_code 201</code> for created success status response code that indicates the request has succeeded.</p>
</li>
</ul>
<p>Save the <code>run.py</code> script file by pressing Ctrl-o, the Enter key, and Ctrl-x.</p>
<p>Grant executable permission to the run.py script.</p>
<pre><code>chmod +x ~/run.py&#x000A;</code></pre>
<p>Now, run the <code>run.py</code> script:</p>
<pre><code>./run.py&#x000A;</code></pre>
<p>Your POST requests should have successfully uploaded the feedback on the company's website. Now, visit the website again using the <code>corpweb</code> external IP address or just refresh the page if already opened, and you should be able to see the feedback.</p>
<p><img alt="7639cece365f6956.png" src="https://cdn.qwiklabs.com/RBlUCcCZl3ldcQbpDrRNe9%2Fh9w4RM24kgQ7wAFuvsjM%3D"></p>
