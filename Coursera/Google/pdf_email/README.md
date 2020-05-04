<h1 class='lab-preamble__title'>
Automatically Generate a PDF and send it by Email
</h1>
<div class='lab-preamble__details subtitle-headline-1'>
<span>1 hour 30 minutes</span>
<span>Free</span>
<div class='lab-content__inner-wrapper'>
<div class='js-markdown-instructions lab-content__markdown markdown-lab-instructions' id='markdown-lab-instructions'>
<h2 id="step1">Introduction</h2>
<p>You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.</p>
<h3>What you'll do</h3>
<ul>
<li>Write a script that summarizes and processes sales data into different categories</li>
<li>Generate a PDF using Python</li>
<li>Automatically send a PDF by email</li>
</ul>
<p>You'll have 90 minutes to complete this lab.</p>
<h2 id="step3">Sample report</h2>
<p>In this section, you will be creating a PDF report named "<strong>A Complete Inventory of My Fruit</strong>". The script to generate this report and send it by email is already pre-done. You can have a look at the script in the <code>scripts/</code> directory.</p>
<pre><code>ls ~/scripts&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="d88741641edb4e4e.png" src="https://cdn.qwiklabs.com/rUInm6B0Qy3UeH1XXEKCEVy2UZy4e1uZYzGiRqs%2BbA8%3D"></p>
<p>In the <code>scripts/</code> directory, you will find <code>reports.py</code> and <code>emails.py</code> files. These files are used to <strong>generate PDF files</strong> and <strong>send emails</strong> respectively.</p>
<p>Take a look at these files using <code>cat</code> command.</p>
<pre><code>cat ~/scripts/reports.py&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="86bd37a685f9718e.png" src="https://cdn.qwiklabs.com/i56VdMuHLeKKX3Os%2BNgWUppDi4eysFfbqvSqMTu3J8w%3D"></p>
<pre><code>cat ~/scripts/emails.py&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="a8e8db253f010864.png" src="https://cdn.qwiklabs.com/gF3Hv%2B59YaeH2he4EtWf1Fb6LkH989IlBv%2FpBgnOtlI%3D"></p>
<p>Now, take a look at <code>example.py</code>, which uses these two modules <strong>reports</strong> and <strong>emails</strong> to create a report and then send it by email.</p>
<pre><code>cat ~/scripts/example.py&#x000A;</code></pre>
<p>Grant executable permission to the <code>example.py</code> script.</p>
<pre><code>sudo chmod o+wx ~/scripts/example.py&#x000A;</code></pre>
<p>Run the <code>example.py</code> script, which will generate mail to you.</p>
<pre><code>./scripts/example.py&#x000A;</code></pre>
<p>A mail should now be successfully sent.</p>
<p>Copy the <code>external IP address</code> of your instance from the Connection Details Panel on the left side and open a new web browser tab and enter the IP address. The Roundcube Webmail login page appears.</p>
<p>Here, you'll need a login to <strong>roundcube</strong> using the username and password mentioned in the Connection Details Panel on the left hand side, followed by clicking <strong>Login</strong>.</p>
<p><img alt="10a23ccdb979a002.png" src="https://cdn.qwiklabs.com/OXW2yZtaYTQ%2BZTVIcMUspBmZBCkBmmTQUEppra6WwMI%3D"></p>
<p>Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.</p>
<p>Output:</p>
<p><img alt="41a28598157d4729.png" src="https://cdn.qwiklabs.com/Jkzel%2BFKxrzSvwCNotGofHYqCi3Nztd2GEWTcGAirY0%3D"></p>
<h3>Generate report</h3>
<p>Now, let's make a couple of changes in the <code>example.py</code> file to add a new fruit and change the sender followed by granting editor permission. Open <code>example.py</code> file using the following command:</p>
<pre><code>nano ~/scripts/example.py&#x000A;</code></pre>
<p>And update the following variables:</p>
<table>
<tr>
<td colspan="1" rowspan="1">
<p><strong>variable_name</strong></p>
</td>
<td colspan="1" rowspan="1">
<p><strong>value</strong></p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>sender</p>
</td>
<td colspan="1" rowspan="1">
<p>Replace <strong>sender@example.com</strong> with  <strong>automation@example.com</strong></p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>table_data</p>
</td>
<td colspan="1" rowspan="1">
<p>Add another entry into the list: <code>['kiwi', 4, 0.49]</code></p>
</td>
</tr>
</table>
<p>The file should now look similar to:</p>
<pre><code>#!/usr/bin/env python3&#x000A;import emails&#x000A;import os&#x000A;import reports&#x000A;table_data=[&#x000A;  ['Name', 'Amount', 'Value'],&#x000A;  ['elderberries', 10, 0.45],&#x000A;  ['figs', 5, 3],&#x000A;  ['apples', 4, 2.75],&#x000A;  ['durians', 1, 25],&#x000A;  ['bananas', 5, 1.99],&#x000A;  ['cherries', 23, 5.80],&#x000A;  ['grapes', 13, 2.48],&#x000A;  ['kiwi', 4, 0.49]]&#x000A;reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)&#x000A;sender = "automation@example.com"&#x000A;receiver = "{}@example.com".format(os.environ.get('USER'))&#x000A;subject = "List of Fruits"&#x000A;body = "Hi\n\nI'm sending an attachment with all my fruit."&#x000A;message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")&#x000A;emails.send(message)&#x000A;</code></pre>
<p>Once you've made the changes in the <code>example.py</code> script, save the file by typing  <strong>Ctrl-o</strong>, <strong>Enter</strong> key and <strong>Ctrl-x</strong>.</p>
<p>Now execute the example script again.</p>
<pre><code>./scripts/example.py&#x000A;</code></pre>
<p>Now, check the webmail for any new mail. You can click on the <strong>Refresh</strong> button to refresh your inbox.</p>
<p><img alt="6f55d4c2f3ad0c4.png" src="https://cdn.qwiklabs.com/x4bb%2B2%2Fkwck7d7SXgVjzbmHiqAhVFyLsKzwugFGGpQ4%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="1">
Generate sample report
</ql-activity-tracking></p>
<h2 id="step4">Sales summary</h2>
<p>In this section, let's view the summary of last month's sales for all the models offered by the company. This data is in a JSON file named <code>car_sales.json</code>. Let's have a look at it.</p>
<pre><code>cat car_sales.json&#x000A;</code></pre>
<p>Output:</p>
<p><img alt="dccac1f426670528.png" src="https://cdn.qwiklabs.com/A2aAqrGDdDqk0sbLXhXAl%2FluSkUdrypVdWv5qYyRgwo%3D"></p>
<p>To simplify the JSON structure, here is an example of one of the JSON objects among the list.</p>
<pre><code>{&#x000A;        "id": 47,&#x000A;        "car": {&#x000A;                "car_make": "Lamborghini",&#x000A;                "car_model": "Murciélago",&#x000A;                "car_year": 2002&#x000A;        },&#x000A;        "price": "$13724.05",&#x000A;        "total_sales": 149&#x000A;}&#x000A;</code></pre>
<p>Here <code>id, car, price and total_sales</code> are the field names (key).</p>
<p>The script <code>cars.py</code> already contains part of the work, but learners need to complete the task by writing the remaining pieces. The script already calculates the car model with the most revenue (price * total_sales) in the <code>process_data</code> method. Learners need to add the following:</p>
<ol>
<li>
<p>Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the <code>summary</code> list in the below format:</p>
</li>
</ol>
<ul>
<li>
<p>"The {car model} had the most sales: {total sales}"</p>
</li>
</ul>
<ol start="2">
<li>
<p>Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year) by completing the <code>process_data</code> method, and append a formatted string to the <code>summary</code> list in the below format:</p>
</li>
</ol>
<ul>
<li>
<p>"The most popular year was {year} with {total sales in that year} sales."</p>
</li>
</ul>
<h3>The challenge</h3>
<p>Here, you are going to update the script <code>cars.py</code>. You will be using the above JSON data to process information. A part of the script is already done for you, where it calculates the car model with the most revenue (price * total_sales). You should now fulfil the following objectives with the script:</p>
<ol>
<li>Calculate the car model which had the most sales.</li>
</ol>
<p>a. Call <code>format_car</code> method for the car model.</p>
<ol start="2">
<li>Calculate the most popular car_year across all car make/models.</li>
</ol>
<ql-infobox><strong>Hint:</strong> Find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year.</ql-infobox>
<p>Grant required permissions to the file <code>cars.py</code> and open it using nano editor.</p>
<pre><code>sudo chmod o+wx ~/scripts/cars.py&#x000A;</code></pre>
<pre><code>nano ~/scripts/cars.py&#x000A;</code></pre>
<p>The code is well commented including the TODO sections for you to understand and fulfill the objectives.</p>
<h3>Generate PDF and send Email</h3>
<p>Once the data is collected, you will also need to further update the script to generate a PDF report and automatically send it through email.</p>
<p>To generate a PDF:</p>
<ul>
<li>
<p>Use the <code>reports.generate()</code> function within the main function.</p>
</li>
<li>
<p>The report should be named as <strong>cars.pdf</strong>, and placed in the folder <strong>/tmp/</strong>.</p>
</li>
<li>
<p>The PDF should contain:</p>
<ol>
<li>A summary paragraph which contains the most sales/most revenue/most popular year values worked out in the previous step.</li>
</ol>
<ql-infobox><strong>Note:</strong> To add line breaks in the PDF, use: &lt;br/&gt; between the lines.</ql-infobox>
<ol start="2">
<li>A table which contains all the information parsed from the JSON file, organised by id_number. The car details should be combined into one column in the form &lt;car_make&gt; &lt;car_model&gt; (&lt;car_year&gt;).</li>
</ol>
<ql-infobox><strong>Note:</strong> You can use the <strong>cars_dict_to_table</strong> function for the above task.</ql-infobox>
</li>
</ul>
<p>Example:</p>
<table>
<tr>
<td colspan="1" rowspan="1">
<p><strong>ID</strong></p>
</td>
<td colspan="1" rowspan="1">
<p><strong>Car</strong></p>
</td>
<td colspan="1" rowspan="1">
<p><strong>Price</strong></p>
</td>
<td colspan="1" rowspan="1">
<p><strong>Total Sales</strong></p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>47</p>
</td>
<td colspan="1" rowspan="1">
<p>Acura TL (2007)</p>
</td>
<td colspan="1" rowspan="1">
<p>€14459,15</p>
</td>
<td colspan="1" rowspan="1">
<p>1192</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>73</p>
</td>
<td colspan="1" rowspan="1">
<p>Porsche 911 (2010)</p>
</td>
<td colspan="1" rowspan="1">
<p>€6057,74</p>
</td>
<td colspan="1" rowspan="1">
<p>882</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>85</p>
</td>
<td colspan="1" rowspan="1">
<p>Mercury Sable (2005)</p>
</td>
<td colspan="1" rowspan="1">
<p>€45660,46</p>
</td>
<td colspan="1" rowspan="1">
<p>874</p>
</td>
</tr>
</table>
<p>To send the PDF through email:</p>
<p>Once the PDF is generated, you need to send the email, using the <code>emails.generate()</code> and <code>emails.send()</code> methods.</p>
<p>Use the following details to pass the parameters to <code>emails.generate()</code>:</p>
<ul>
<li>
<strong>From:</strong> automation@example.com</li>
<li>
<strong>To:</strong> &lt;user&gt;@example.com</li>
<li>
<strong>Subject line</strong>: Sales summary for last month</li>
<li>
<strong>E-mail Body:</strong> The same summary from the PDF, but using <code>\n</code> between the lines</li>
<li>
<strong>Attachment:</strong> Attach the PDF path i.e. generated in the previous step</li>
</ul>
<p>Once you have completed editing <code>cars.py</code> script, save the file by typing <strong>Ctrl-o</strong>, <strong>Enter</strong> key, and <strong>Ctrl-x</strong>.</p>
<p>Run the <code>cars.py</code> script, which will generate mail to their user.</p>
<pre><code>./cars.py&#x000A;</code></pre>
<p>Now, check the webmail for any new mail. You can click on the <strong>Refresh</strong> button to refresh your inbox.</p>
<p>Output:</p>
<p><img alt="e066799de7dd10fe.png" src="https://cdn.qwiklabs.com/EGbZxG2RRNc%2F%2B70k%2FDDPpXB1l6Wza4ZSNTZba4rdYWo%3D"></p>
<p>Open <code>cars.pdf</code> that's located on the right most side.</p>
<p><img alt="15f205f9bf5782f5.png" src="https://cdn.qwiklabs.com/pPYYMs48r3Z3qP7wkDJqi6uiOj%2F3YMtC8%2BH0wAhC0AA%3D"></p>
<p>Click <em>Check my progress</em> to verify the objective.
<ql-activity-tracking step="2">
Challenge: Sales summary
</ql-activity-tracking></p>
