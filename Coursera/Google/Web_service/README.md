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
<p>You'll need to start the lab before you can access the materials in the virtual machine OS.  To do this, click the green “Start Lab” button at the top of the screen.</p>
<ql-infobox><strong>Note:</strong> For this lab you are going to access the <strong>Linux VM</strong> through your <strong>local SSH Client</strong>, and not use the <strong>Google Console</strong> (<strong>Open GCP Console</strong> button is not available for this lab).</ql-infobox>
<p><img alt="Start Lab" src="https://cdn.qwiklabs.com/dvIz%2BhCdCLq0P9JbORQrHU9h22GU18bW7Bo%2FMfQPoSs%3D"></p>
<p>After you click the “Start Lab” button, you will see all the SSH connection details on the left-hand side of your screen. You should have a screen that looks like this:</p>
<p><img alt="Connection details" src="https://cdn.qwiklabs.com/T2WTv35A3yGYeomHD1stDaAZpBpVymNqc380RdOBVe4%3D"></p>
<h2 id="step2">Accessing the virtual machine</h2>
<p>Please find one of the three relevant options below based on your device's operating system.</p>
<ql-infobox><strong>Note:</strong> Working with Qwiklabs may be similar to the work you'd perform as an <strong>IT Support Specialist</strong>; you'll be interfacing with a cutting-edge technology that requires multiple steps to access, and perhaps healthy doses of patience and persistence(!). You'll also be using <strong>SSH</strong> to enter the labs -- a critical skill in IT Support that you’ll be able to practice through the labs.</ql-infobox>
<h3>Option 1: Windows Users: Connecting to your VM</h3>
<p>In this section, you will use the PuTTY Secure Shell (SSH) client and your VM’s External IP address to connect.</p>
<p><strong>Download your PPK key file</strong></p>
<p>You can download the VM’s private key file in the PuTTY-compatible <strong>PPK</strong> format from the Qwiklabs Start Lab page. Click on <strong>Download PPK</strong>.</p>
<p><img alt="PPK" src="https://cdn.qwiklabs.com/ZWdhDzmDeppdXplN8b2GE%2BJ4HjiEs50sjhmD9fIWS1o%3D"></p>
<p><strong>Connect to your VM using SSH and PuTTY</strong></p>
<ol>
<li>
<p>You can download Putty from <a href="https://the.earth.li/%7Esgtatham/putty/latest/w64/putty.exe">here</a></p>
</li>
<li>
<p>In the <strong>Host Name (or IP address)</strong> box, enter username@external_ip_address.</p>
</li>
</ol>
<ql-infobox><strong>Note:</strong> Replace <strong>username</strong> and <strong>external_ip_address</strong> with values provided in the lab.</ql-infobox>
<p><img alt="Putty_1" src="https://cdn.qwiklabs.com/9WwXv1tzK%2BUCbpUECb94LBndveI2BCYa9uDRGzctoLg%3D"></p>
<ol start="3">
<li>
<p>In the <strong>Category</strong> list, expand <strong>SSH</strong>.</p>
</li>
<li>
<p>Click <strong>Auth</strong> (don’t expand it).</p>
</li>
<li>
<p>In the <strong>Private key file for authentication</strong> box, browse to the PPK file that you downloaded and double-click it.</p>
</li>
<li>
<p>Click on the <strong>Open</strong> button.</p>
</li>
</ol>
<ql-infobox><strong>Note:</strong> PPK file is to be imported into PuTTY tool using the Browse option available in it. It should not be opened directly but only to be used in PuTTY.</ql-infobox>
<p><img alt="Putty_2" src="https://cdn.qwiklabs.com/MwC8aAcTUdtsEuTl2v2DSI7YSCshINv%2Fgzm4ZCSrQig%3D"></p>
<ol start="7">
<li>Click <strong>Yes</strong> when prompted to allow a first connection to this remote SSH server. Because you are using a key pair for authentication, you will not be prompted for a password.</li>
</ol>
<p><strong>Common issues</strong></p>
<p>If PuTTY fails to connect to your Linux VM, verify that:</p>
<ul>
<li>
<p>You entered <strong>&lt;username&gt;</strong>@<strong>&lt;external ip address&gt;</strong> in PuTTY.</p>
</li>
<li>
<p>You downloaded the fresh new PPK file for this lab from Qwiklabs.</p>
</li>
<li>
<p>You are using the downloaded PPK file in PuTTY.</p>
</li>
</ul>
<h3>Option 2: OSX and Linux users: Connecting to your VM via SSH</h3>
<p><strong>Download your VM’s private key file.</strong></p>
<p>You can download the private key file in PEM format from the Qwiklabs Start Lab page. Click on <strong>Download PEM</strong>.</p>
<p><img alt="PEM" src="https://cdn.qwiklabs.com/TZ4BSQDq%2Bw742PSPxwNDKIMY180rPQHbNISmuG59wP8%3D"></p>
<p><strong>Connect to the VM using the local Terminal application</strong></p>
<p>A <strong>terminal</strong> is a program which provides a <strong>text-based interface for typing commands</strong>. Here you will use your terminal as an SSH client to connect with lab provided Linux VM.</p>
<ol>
<li>
<p>Open the Terminal application.</p>
<ul>
<li>
<p>To open the terminal in Linux use the shortcut key <strong>Ctrl+Alt+t</strong>.</p>
</li>
<li>
<p>To open terminal in <strong>Mac</strong> (OSX) enter <strong>cmd + space</strong> and search for <strong>terminal</strong>.</p>
</li>
</ul>
</li>
<li>
<p>Enter the following commands.</p>
</li>
</ol>
<ql-infobox><strong>Note:</strong> Substitute the <strong>path/filename for the PEM</strong> file you downloaded, <strong>username</strong> and <strong>External IP Address</strong>.</ql-infobox>
<p>You will most likely find the PEM file in <strong>Downloads</strong>. If you have not changed the download settings of your system, then the path of the PEM key will be <strong>~/Downloads/qwikLABS-XXXXX.pem</strong></p>
<pre><code>chmod 600 ~/Downloads/qwikLABS-XXXXX.pem&#x000A;</code></pre>
<pre><code>ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address&#x000A;</code></pre>
<p><img alt="SSH" src="https://cdn.qwiklabs.com/H7KOW2FkxOOgsLdxMuZWTl2PoqPlgElnb0YQtC319hQ%3D"></p>
<h3>Option 3: Chrome OS users: Connecting to your VM via SSH</h3>
<ql-infobox><strong>Note:</strong> Make sure you are not in <strong>Incognito/Private mode</strong> while launching the application.</ql-infobox>
<p><strong>Download your VM’s private key file.</strong></p>
<p>You can download the private key file in PEM format from the Qwiklabs Start Lab page. Click on <strong>Download PEM</strong>.</p>
<p><img alt="PEM" src="https://cdn.qwiklabs.com/TZ4BSQDq%2Bw742PSPxwNDKIMY180rPQHbNISmuG59wP8%3D"></p>
<p><strong>Connect to your VM</strong></p>
<ol>
<li>
<p>Add Secure Shell from  <a href="https://chrome.google.com/webstore/detail/secure-shell-app/pnhechapfaindjhompbnflcldabbghjo" target="_blank">here</a> to your Chrome browser.</p>
</li>
<li>
<p>Open the Secure Shell app and click on <strong>[New Connection]</strong>.</p>
<p><img alt="new-connection-button" src="https://cdn.qwiklabs.com/5wIwLwU6D1mNWkeYsNVEazGLRrzuWsUq6t6%2F1NnWqcM%3D"></p>
</li>
<li>
<p>In the <strong>username</strong> section, enter the username given in the Connection Details Panel of the lab. And for the <strong>hostname</strong> section, enter the external IP of your VM instance that is mentioned in the Connection Details Panel of the lab.</p>
<p><img alt="username-hostname-fields" src="https://cdn.qwiklabs.com/fymsGw1B5jFEANsD41CD5dFrPWa9ASKnqfoVONtOxlA%3D"></p>
</li>
<li>
<p>In the <strong>Identity</strong> section, import the downloaded PEM key by clicking on the <strong>Import…</strong> button beside the field. Choose your PEM key and click on the <strong>OPEN</strong> button.</p>
</li>
</ol>
<ql-infobox><strong>Note:</strong> If the key is still not available after importing it, refresh the application, and select it from the <strong>Identity</strong> drop-down menu.
</ql-infobox>
<ol start="5">
<li>
<p>Once your key is uploaded, click on the <strong>[ENTER] Connect</strong> button below.</p>
<p><img alt="import-button" src="https://cdn.qwiklabs.com/knW0T7QscQZ6VVTUPKW%2FkF4LERKArqDwSQqWnF8GxV8%3D"></p>
</li>
<li>
<p>For any prompts, type <strong>yes</strong> to continue.</p>
</li>
<li>
<p>You have now successfully connected to your Linux VM.</p>
</li>
</ol>
<p>You're now ready to continue with the lab!</p>

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
