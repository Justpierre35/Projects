<h1>Automate updating catalog information
</h1>
<div class='lab-preamble__details subtitle-headline-1'>
<span>2 hours </span>
<span>Free</span>
<div class='lab__rating'>
<a href="/focuses/52114/reviews?parent=catalog"><div class='rateit' data-rateit-readonly='true' data-rateit-value='3.9578'></div>

</a><a data-target='#lab-review-modal' data-toggle='modal'>
Rate Lab
</a>
</div>
</div>
</div>

<div class='lab-content__inner-wrapper'>
<div class='js-markdown-instructions lab-content__markdown markdown-lab-instructions' id='markdown-lab-instructions'>



<h2 id="step1">Introduction</h2>
<p>You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.</p>
<p>You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.</p>
<p>Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).</p>
<p>Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.</p>
<h3>What you'll do</h3>
<ul>
<li>Write a script that summarizes and processes sales data into different categories</li>
<li>Generate a PDF using Python</li>
<li>Automatically send a PDF by email</li>
<li>Write a script to check the health status of the system</li>
</ul>
<p>You'll have 120 minutes to complete this lab.</p>
<h2 id="step3">Fetching supplier data</h2>
<p>You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).</p>
<p>Here, you'll find two script files <code>download_drive_file.sh</code> and the <code>example_upload.py</code> files. You can view it by using the following command.</p>
<pre><code>ls ~/&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="19cdba5cb97d3091.png" src="https://cdn.qwiklabs.com/oZa6n6ycZXfdecHuhLeD9euSrlh%2Fefq7A6qzL2zx4ug%3D"></p>
<p>To download the file from the supplier onto our <code>linux-instance</code> virtual machine we will first grant executable permission to the <code>download_drive_file.sh</code> script.</p>
<pre><code>sudo chmod +x ~/download_drive_file.sh&#x000A;</code></pre>
<p>Run the <code>download_drive_file.sh</code> shell script with the following arguments:</p>
<pre><code>./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="fa96a73a09a0fb81.png" src="https://cdn.qwiklabs.com/cY7GAoO%2FDl5UHWHlnjNcpZtC3Zo8NzMN6hFcdAvfNDU%3D"></p>
<p>You have now downloaded a file named <code>supplier-data.tar.gz</code> containing the supplier's data. Let's extract the contents from this file using the following command:</p>
<pre><code>tar xf ~/supplier-data.tar.gz&#x000A;</code></pre>
<p>This creates a directory named <code>supplier-data</code>, that contains subdirectories named <code>images</code> and <code>descriptions</code>.</p>
<p><img alt="2ba417715369f867.png" src="https://cdn.qwiklabs.com/5ft5dMC5m7MF2HDYCSg%2BZ5Q9pfYgMFzUOSgqu0aWECo%3D"></p>
<p>List contents of the <code>supplier-data</code> directory using the following command:</p>
<pre><code>ls ~/supplier-data&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="3fb0e0016e2bb0f7.png" src="https://cdn.qwiklabs.com/HTrio1kwEPHbufRsHN%2BjTDd7vkef4o32I9UWm3Jl9VA%3D"></p>
<p>The subdirectory <code>images</code> contain images of various fruits, while the <code>descriptions</code> subdirectory has text files containing the description of each fruit. You can have a look at any of these text files using <code>cat</code> command.</p>
<pre><code>cat ~/supplier-data/descriptions/007.txt&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="3047a30cc5caf228.png" src="https://cdn.qwiklabs.com/nVGspBqLFe%2BBtyTK2EDZu3rLxFJr30tgPez%2Blbbp9fQ%3D"></p>
<p>The first line contains the name of the fruit followed by the weight of the fruit and finally the description of the fruit.</p>
<h2 id="step4">Working with supplier images</h2>
<p>In this section, you will write a Python script named <code>changeImage.py</code> to process the supplier images. You will be using the PIL library to update all images within ~<code>/supplier-data/images</code> directory to the following specifications:</p>
<ul>
<li>
<strong>Size</strong>: Change image resolution from <strong>3000x2000</strong> to <strong>600x400</strong> pixel</li>
<li>
<strong>Format</strong>: Change image format from <strong>.TIFF</strong> to <strong>.JPEG</strong>
</li>
</ul>
<p>Create and open the file using nano editor.</p>
<pre><code>nano ~/changeImage.py&#x000A;</code></pre>
<p>Add a shebang line in the first line.</p>
<pre><code>#!/usr/bin/env python3&#x000A;</code></pre>
<p>This is the challenge section, where you will be writing a script that satisfies the above objectives.</p>
<ql-infobox><strong>Note:</strong> The raw images from <code>images</code> subdirectory contains alpha transparency layers. So, it is better to first convert <code>RGBA</code> 4-channel format to <code>RGB</code> 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.</ql-infobox>
<p>After processing the images, save them in the same path <code>~/supplier-data/images</code>, with a JPEG extension.</p>
<p>Once you have completed editing the <code>changeImage.py</code> script, save the file by clicking <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Grant executable permissions to the <code>changeImage.py</code> script.</p>
<pre><code>sudo chmod +x ~/changeImage.py&#x000A;</code></pre>
<p>Now run the <code>changeImage.py</code> script:</p>
<pre><code>./changeImage.py&#x000A;</code></pre>
<p>Now, let's check the specifications of the images you just updated. Open any image using the following command:</p>
<pre><code>file ~/supplier-data/images/003.jpeg&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="48b82d8d8a4f3c51.png" src="https://cdn.qwiklabs.com/nE8H4Vo8aI5yHiEuRy86b0Wb9soj144dHeNhYejdFq0%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="1">
Update image specifications
</ql-activity-tracking></p>
<h2 id="step5">Uploading images to web server</h2>
<p>You have modified the fruit images through <code>changeImage.py</code> script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python <code>requests</code> module to send the file contents to the <code>[linux-instance-IP-Address]/upload</code> URL.</p>
<p>Copy the <code>external IP address</code> of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "<code>Fruit Catalog</code>".</p>
<p>In the home directory, you'll have a script named <code>example_upload.py</code> to upload images to the running fruit catalog web server. To view the <code>example_upload.py</code> script use the <code>cat</code> command.</p>
<pre><code>cat ~/example_upload.py&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="d1a53f8b31586d73.png" src="https://cdn.qwiklabs.com/9yJABmfzWCPRfvhKEPYiqdR9teLcxpG%2Bn8xaenQbucs%3D"></p>
<p>In this script, we are going to upload a sample image named <code>icon.sheet.png</code>.</p>
<p>Grant executable permission to the <code>example_upload.py</code> script.</p>
<pre><code>sudo chmod +x ~/example_upload.py&#x000A;</code></pre>
<p>Execute the <code>example_upload.py</code> script, which will upload the images.</p>
<pre><code>./example_upload.py&#x000A;</code></pre>
<p>Now check out that the file <code>icon.sheet.png</code> was uploaded to the web server by visiting the URL <code>[linux-instance-IP-Address]/media/images/</code>, followed by clicking on the file name.</p>
<p>Output:</p>
<p><img alt="2ff93301dabfc549.png" src="https://cdn.qwiklabs.com/rEdNe73TPnSnB4aiLMzl0clBHTeYHWrwRNEYTL2EEm4%3D"></p>
<p>In a similar way, you are going to write a script named <code>supplier_image_upload.py</code> that takes the <strong>jpeg</strong> images from the <code>supplier-data/images</code> directory that you've processed previously and uploads them to the web server fruit catalog.</p>
<p>Use the nano editor to create a file named <code>supplier_image_upload.py</code>:</p>
<pre><code>nano ~/supplier_image_upload.py&#x000A;</code></pre>
<p>Complete the script with the same technique as used in the file <code>example_upload.py</code>.</p>
<p>Once you have completed editing the <code>supplier_image_upload.py</code> script, save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Grant executable permission to the <code>changeImage.py</code> script.</p>
<pre><code>sudo chmod +x ~/supplier_image_upload.py&#x000A;</code></pre>
<p>Run the <code>changeImage.py</code> script.</p>
<pre><code>./supplier_image_upload.py&#x000A;</code></pre>
<p>Refresh the URL opened earlier, and now you should find all the images uploaded successfully.</p>
<p>Output:</p>
<p><img alt="1664f43929363847.png" src="https://cdn.qwiklabs.com/D21DfEDXkfgBjiVA2%2FNjHedxh22tBmPLhx61U2GkXbw%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="2">
Upload images to the web server
</ql-activity-tracking></p>
<h2 id="step6">Uploading the descriptions</h2>
<p>The Django server is already set up to show the fruit catalog for your company. You can visit the main website by entering <code>linux-instance-IP-Address</code> in the URL bar or by removing /media/images from the existing URL opened earlier. The interface looks like this:</p>
<p><img alt="3c3e31b6d0ca1038.png" src="https://cdn.qwiklabs.com/JWxbvtE2tFc%2F0cgPNlv8%2F1xYgnpDxjmXjR2gI%2FlUP44%3D"></p>
<p>Check out the Django REST framework, by navigating to <code>linux-instance-IP-Address/fruits</code> in your browser.</p>
<p><img alt="44aaa38049449875.png" src="https://cdn.qwiklabs.com/ZPQ%2BmfewKIAeESZLRCjUkjqmZ5DQFKxxmkHVKhtirnk%3D"></p>
<p>Currently, there are no products in the fruit catalog web-server. You can create a test fruit entry by entering the following into the <strong>content</strong> field:</p>
<p><code>{"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}</code></p>
<p>After entering the above data into the content field click on the POST button. Now visit the main page of your website (by going to <code>http://[linux-instance-external-IP]/</code>), and the new test fruit you uploaded appears.</p>
<p><img alt="d72416aaf9bb08c3.png" src="https://cdn.qwiklabs.com/ZxpDdwsTvAW48PonnnIRepsamtLOQNztvqhzhKgrnro%3D"></p>
<p>To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the <strong>fruit images</strong> and their respective <strong>description</strong> in JSON format.</p>
<p>Write a Python script named <code>run.py</code> to process the text files (001.txt, 003.txt ...) from the <code>supplier-data/descriptions</code> directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to <code>http://[linux-instance-external-IP]/fruits</code> using the Python <strong>requests</strong> library.</p>
<p>Create <code>run.py</code> using the nano editor:</p>
<pre><code>nano ~/run.py&#x000A;</code></pre>
<p>Add the shebang line and import necessary libraries.</p>
<pre><code>#! /usr/bin/env python3&#x000A;</code></pre>
<pre><code>import os&#x000A;import requests&#x000A;</code></pre>
<p>Now, you'll have to process the .txt files (named <code>001.txt, 002.txt, ...</code>) in the <code>supplier-data/descriptions/</code> directory and save them in a data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:</p>
<ul>
<li>name</li>
<li>weight (in lbs)</li>
<li>description</li>
</ul>
<p>The data model in the Django application <code>fruit</code> has the following fields: <code>name</code>, <code>weight</code>, <code>description</code> and <code>image_name</code>. The <code>weight</code> field is defined as an <strong>integer</strong> field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "<strong>500 lbs</strong>", you need to <strong>drop "lbs"</strong> and <strong>convert "500" to an integer</strong>.</p>
<p>The <code>image_name</code> field will allow the system to find the image associated with the fruit. Don't forget to add all fields, including the <code>image_name</code>! The final JSON object should be similar to:</p>
<p><code>{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}</code></p>
<p>Iterate over all the fruits and use <strong>post</strong> method from Python requests library to upload all the data to the URL <code>http://[linux-instance-external-IP]/fruits</code></p>
<p>Once you complete editing <code>run.py</code> script, save the file by clicking <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Grant executable permission to the <code>run.py</code> script.</p>
<pre><code>sudo chmod +x ~/run.py&#x000A;</code></pre>
<p>Run the <code>run.py</code> script:</p>
<pre><code>./run.py&#x000A;</code></pre>
<p>Now go to the main page of your website (by going to <code>http://[linux-instance-IP-Address]/</code>) and check out how the new fruits appear.</p>
<p><img alt="202677b175787ed9.png" src="https://cdn.qwiklabs.com/T6xJ3BXTcGFy%2FTfQ8B25zRLl4ffCStGL6XCjDLHiUPs%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="3">
Upload the descriptions
</ql-activity-tracking></p>
<h2 id="step7">Generate a PDF report and send it through email</h2>
<p>Once the <code>images</code> and <code>descriptions</code> have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the <code>ReportLab</code> library. The content of the report should look like this:</p>
<p><strong>Processed Update on &lt;Today's date&gt;</strong></p>
<p>[blank line]</p>
<p>name: Apple</p>
<p>weight: 500 lbs</p>
<p>[blank line]</p>
<p>name: Avocado</p>
<p>weight: 200 lbs</p>
<p>[blank line]</p>
<p>...</p>
<h3>Script to generate a PDF report</h3>
<p>Create a script <code>reports.py</code> to generate PDF report to supplier using the nano editor:</p>
<pre><code>nano ~/reports.py&#x000A;</code></pre>
<p>Add a shebang line in the first line.</p>
<pre><code>#!/usr/bin/env python3&#x000A;</code></pre>
<p>Using the <code>reportlab</code> Python library, define the method <code>generate_report</code> to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named <strong>processed.pdf</strong>.</p>
<p>Once you have finished editing the script <code>reports.py</code>, save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Create another script named <code>report_email.py</code> to process supplier fruit description data from <code>supplier-data/descriptions</code> directory. Use the following command to create <code>report_email.py</code>.</p>
<pre><code>nano ~/report_email.py&#x000A;</code></pre>
<p>Add a shebang line.</p>
<pre><code>#!/usr/bin/env python3&#x000A;</code></pre>
<p>Import all the necessary libraries(<code>os</code>, <code>datetime</code> and <code>reports</code>) that will be used to process the text data from the <code>supplier-data/descriptions</code> directory into the format below:</p>
<p>name: Apple</p>
<p>weight: 500 lbs</p>
<p>[blank line]</p>
<p>name: Avocado</p>
<p>weight: 200 lbs</p>
<p>[blank line]</p>
<p>...</p>
<p>Once you have completed this, call the main method which will process the data and call the <code>generate_report</code> method from the <code>reports</code> module:</p>
<pre><code>if __name__ == "__main__":&#x000A;</code></pre>
<p>You will need to pass the following arguments to the <code>reports.generate_report</code> method: the text description processed from the text files as the <code>paragraph</code> argument, the report title as the <code>title</code> argument, and the file path of the PDF to be generated as the <code>attachment</code> argument (use ‘<code>/tmp/processed.pdf</code>')</p>
<pre><code>  reports.generate_report(attachment, title, paragraph)&#x000A;</code></pre>
<p>Once you have completed the <code>report_email.py</code> script. Save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<h3>Send report through email</h3>
<p>Once the PDF is generated, you need to send the email using the <code>emails.generate_email()</code> and <code>emails.send_email()</code> methods.</p>
<p>Create <code>emails.py</code> using the nano editor using the following command:</p>
<pre><code>nano ~/emails.py&#x000A;</code></pre>
<p>Define <code>generate_email</code> and <code>send_email</code> methods by importing necessary libraries.</p>
<p>Once you have finished editing the <code>emails.py</code> script, save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Now, open the <code>report_email.py</code> script using the nano editor:</p>
<pre><code>nano ~/report_email.py&#x000A;</code></pre>
<p>Once you define the <code>generate_email</code> and <code>send_email</code> methods, call the methods under the main method after creating the PDF report:</p>
<pre><code>if __name__ == "__main__":&#x000A;</code></pre>
<p>Use the following details to pass the parameters to <code>emails.generate_email()</code>:</p>
<ul>
<li>
<strong>From:</strong> automation@example.com</li>
<li>
<strong>To:</strong> <a href="mailto:username@example.com">username@example.com</a>
<ul>
<li>Replace <code>username</code> with the <code>username</code> given in the Connection Details Panel on the right hand side.</li>
</ul>
</li>
<li>
<strong>Subject line</strong>: Upload Completed - Online Fruit Store</li>
<li>
<strong>E-mail Body:</strong> All fruits are uploaded to our website successfully. A detailed list is attached to this email.</li>
<li>
<strong>Attachment:</strong> Attach the path to the file <code>processed.pdf</code>
</li>
</ul>
<p>Once you have finished editing the <code>report_email.py</code> script, save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Grant executable permissions to the script <code>report_email.py</code>.</p>
<pre><code>sudo chmod +x ~/report_email.py&#x000A;</code></pre>
<p>Run the <code>report_email.py</code> script.</p>
<pre><code>./report_email.py&#x000A;</code></pre>
<p>Now, check the webmail by visiting <code>[linux-instance-external-IP]/webmail</code>. Here, you'll need a login to <strong>roundcube</strong> using the username and password mentioned in the Connection Details Panel on the left hand side, followed by clicking <strong>Login</strong>.</p>
<p>Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.</p>
<p>Output:</p>
<p><img alt="20ecb14552c7fd28.png" src="https://cdn.qwiklabs.com/JxgPNyddBbHW4tIT1XD6chuuJOtcTBR4obwZc9MBneA%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="4">
Generate PDF and send through email
</ql-activity-tracking></p>
<h2 id="step8">Health check</h2>
<p>This is the last part of the lab, where you will have to write a Python script named <code>health_check.py</code> that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:</p>
<ul>
<li>Report an error if CPU usage is over 80%</li>
<li>Report an error if available disk space is lower than 20%</li>
<li>Report an error if available memory is less than 500MB</li>
<li>Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"</li>
</ul>
<p>Create a python script named <code>health_check.py</code> using the nano editor:</p>
<pre><code>nano ~/health_check.py&#x000A;</code></pre>
<p>Add a shebang line.</p>
<pre><code>#!/usr/bin/env python3&#x000A;</code></pre>
<p>Import the necessary Python libraries (eg. shutil, psutil) to write this script.</p>
<p>Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:</p>
<ul>
<li>
<strong>From:</strong> automation@example.com</li>
<li>
<strong>To:</strong> <a href="mailto:username@example.com">username@example.com</a>
<ul>
<li>Replace <code>username</code> with the <code>username</code> given in the Connection Details Panel on the right hand side.</li>
</ul>
</li>
<li>
<strong>Subject line</strong>:
<table>
<tr>
<td colspan="1" rowspan="1">
<p><strong>Case</strong></p>
</td>
<td colspan="1" rowspan="1">
<p><strong>Subject line</strong></p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>CPU usage is over 80%</p>
</td>
<td colspan="1" rowspan="1">
<p>Error - CPU usage is over 80%</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>Available disk space is lower than 20%</p>
</td>
<td colspan="1" rowspan="1">
<p>Error - Available disk space is less than 20%</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>available memory is less than 500MB</p>
</td>
<td colspan="1" rowspan="1">
<p>Error - Available memory is less than 500MB</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>hostname "localhost" cannot be resolved to "127.0.0.1"</p>
</td>
<td colspan="1" rowspan="1">
<p>Error - localhost cannot be resolved to 127.0.0.1</p>
</td>
</tr>
</table>
</li>
<li>
<strong>E-mail Body:</strong> Please check your system and resolve the issue as soon as possible.</li>
</ul>
<ql-infobox><strong>Note:</strong> There is no attachment file here, so you must be careful while defining the generate_email() method in the <code>emails.py</code> script or you can create a separate generate_error_report() method for handling non-attachment email.</ql-infobox>
<p>Once you have completed the <code>health_check.py</code> script. Save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Grant executable permissions to the script <code>health_check.py</code>.</p>
<pre><code>sudo chmod +x ~/health_check.py&#x000A;</code></pre>
<p>Run the file.</p>
<pre><code>./health_check.py&#x000A;</code></pre>
<p>Next, go to the webmail inbox and refresh it. There should only be an email  something goes wrong, so hopefully you don't see a new email.</p>
<p>Output:</p>
<p><img alt="f9c9477ca64b4b6e.png" src="https://cdn.qwiklabs.com/yCiv8AiTBvFkvQb1o93nAlf2fWkIbS%2FRSOANFxdCYQM%3D"></p>
<p>To test out your script, you can install the <code>stress</code> tool.</p>
<pre><code>sudo apt install stress&#x000A;</code></pre>
<p>Next, call the tool using a good number of CPUs to fully load our CPU resources:</p>
<pre><code>stress --cpu 8&#x000A;</code></pre>
<p>Allow the stress test to run, as it will maximize our CPU utilization. Now run <code>health_check.py</code>  by opening another SSH connection to the <code>linux-instance.</code> Navigate to <code>Accessing the virtual machine</code> on the navigation pane on the right-hand side to open another connection to the instance.</p>
<p>Now run the script:</p>
<pre><code>./health_check.py&#x000A;</code></pre>
<p>Check your inbox for any new email.</p>
<p>Output:</p>
<p><img alt="c179392b8b65cd7f.png" src="https://cdn.qwiklabs.com/17yEGmfRw9VTXyx21kJzkb9TSgPMj9GIaePsLG8siB4%3D"></p>
<p>Open the email with the subject "Error - CPU usage is over 80%" by double clicking it.</p>
<p><img alt="2f3df5a11070691e.png" src="https://cdn.qwiklabs.com/7o7xptowOPJbmcferNUOeYGFQj4EJYvSxEVu8oO%2B2oY%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="5">
Health check
</ql-activity-tracking></p>
<p>Close the <code>stress --cpu</code> command by clicking <strong>Ctrl-c</strong>.</p>
<p>Now, you will be setting a cron job that executes the script <code>health_check.py</code> every 60 seconds and sends health status to the respective user.</p>
<p>To set a user cron job use the following command:</p>
<pre><code>crontab -e&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="crontab-update.png" src="https://cdn.qwiklabs.com/%2FFOC%2BLjj%2BUu03wWQZvjxdxlTdNHPXSMCcEGLQTOB4gM%3D"></p>
<p>Enter 1 to open in the nano editor. Now, set the complete path for <code>health_check.py</code> script, and save by clicking <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Output:</p>
<p><img alt="crontab-edited-image.png" src="https://cdn.qwiklabs.com/U46V%2Fm1wNxLVvuut0fFPAVYTZxdbg%2FMZp28TmcJv4JY%3D"></p>
<h2 id="step9">Congratulations!</h2>
<p>Congrats! You've successfully created a  python script that processes images and descriptions and then updates your company's online website to add the new products. You have also generated a PDF report and sent it by email. Finally, you have also set up monitoring of the system's health.</p>
