#!/usr/bin/python
import csv
outputfile = open("tests_sheets.tex", "w");

# Write document header

with open('docheader.tex', 'r') as infile:
	data=infile.read();
	outputfile.write(data);
# Now write out each test

with open('tests.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"');
	testslist = list(reader);
	row_count = len(testslist);
	x=0;
	outputfile.write("\chapter{Category 1}\n");
	for row in testslist:
		x=x+1;
		if len(row) > 0:
			test_id = testslist[x-1][0];
			number_of_people = testslist[x-1][1];
			who = testslist[x-1][2];
			action = testslist[x-1][3];
			does_what = testslist[x-1][4];
			needed_devices = testslist[x-1][5];
			mesh_extender = testslist[x-1][6];
			when = testslist[x-1][7];
			where = testslist[x-1][8];
			specifics = testslist[x-1][9];
			user_interface = testslist[x-1][10];
			expected_result = testslist[x-1][11];
			st_test_id=str(test_id);	
			if st_test_id[:2]=="T1":
				outputfile.write("\section{Test ID : "+st_test_id+"}\n");
				with open('testheaderT1.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
				# Writing the test needs
				outputfile.write("Test ID : "+st_test_id+"\n This test aims at testing the "+action+" functions of the Serval Software, using "+needed_devices+" with "+specifics+" specifics, in "+where+".\n");
				# Writing the subsection for equipment needed
				outputfile.write("\subsection{Equipment needed} To realise this test, you will need:\n\\begin{itemize}\n\item "+needed_devices+" ;\n\item "+specifics+" specifics;\n\item "+mesh_extender+" mesh extender(s);\n\item "+number_of_people+"\n\end{itemize}\nThis test should be realised in "+where+".\n");
				# Writing the subsection for the operational mode of the test
				# Differentiate between app and captive portal
				tool = user_interface;
				sttool = str(tool);
				if sttool[:10]=="Serval App":
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item Open the App.\n\item Connect to a ME.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the app and switch off the "+needed_devices+".\n");
				else :
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item If a browser didn't open automatically, open one.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the browser and switch off the "+needed_devices+".\n");
				# Writing the expected results and design a sheet
				outputfile.write("\subsection{Expected results} The expected results are "+expected_result+"\n\\newline");

				# Check box for expected results
				outputfile.write("\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\\renewcommand{\\arraystretch}{2.5}\n\centering\n\\begin{tabular}{|M{4cm} M{4.8cm} M{4.8cm}|}\n\n\hline\nCheck ? & $\Box$ Yes & $\Box$ No\\\\ \n\hline \n\end{tabular}\n\\newline\n");

				# Results sheet
				outputfile.write("\\newline\n\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\centering\n\\begin{tabular}{|M{4cm}|M{10cm}|}\n\n\n\hline\nLatency & \\\\[50pt] \n\hline \nRange & \\\\[50pt] \n\hline \n\nBattery Life & \\\\[50pt] \n\hline \nRemarks & \\\\[50pt] \n\hline \nImprovements & \\\\[50pt] \n\hline \n\end{tabular}\n");

				# Writing the test footer
				with open('testfooterT1.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);


	x=0;

	outputfile.write("\chapter{Category 2}\n");
	for row in testslist:
		x=x+1;
		if len(row) > 0:
			value = testslist[x-1][0];
			number_of_people = testslist[x-1][1];
			who = testslist[x-1][2];
			action = testslist[x-1][3];
			does_what = testslist[x-1][4];
			needed_devices = testslist[x-1][5];
			mesh_extender = testslist[x-1][6];
			when = testslist[x-1][7];
			where = testslist[x-1][8];
			specifics = testslist[x-1][9];
			user_interface = testslist[x-1][10];
			expected_result = testslist[x-1][11];
			s=str(value);	
			if s[:2]=="T2":
				outputfile.write("\section{Test ID : "+s+"}\n");
				with open('testheaderT2.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
				# Writing the test needs
				outputfile.write("Test ID : "+s+"\n This test aims at testing the "+action+" functions of the Serval Software, using "+needed_devices+" with "+specifics+" specifics, in "+where+".\n");
				# Writing the subsection for equipment needed
				outputfile.write("\subsection{Equipment needed} To realise this test, you will need:\n\\begin{itemize}\n\item "+needed_devices+" ;\n\item "+specifics+" specifics;\n\item "+mesh_extender+" mesh extender(s);\n\item "+number_of_people+"\n\end{itemize}\nThis test should be realised in "+where+".\n");
				# Writing the subsection for the operational mode of the test
				# Differentiate between app and captive portal
				tool = user_interface;
				sttool = str(tool);
				if sttool[:10]=="Serval App":
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item Open the App.\n\item Connect to a ME.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the app and switch off the "+needed_devices+".\n");
				else :
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item If a browser didn't open automatically, open one.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the browser and switch off the "+needed_devices+".\n");
				# Writing the expected results and design a sheet
				outputfile.write("\subsection{Expected results} The expected results are "+expected_result+"\n\\newline");

				# Check box for expected results
				outputfile.write("\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\\renewcommand{\\arraystretch}{2.5}\n\centering\n\\begin{tabular}{|M{4cm} M{4.8cm} M{4.8cm}|}\n\n\hline\nCheck ? & $\Box$ Yes & $\Box$ No\\\\ \n\hline \n\end{tabular}\n\\newline\n");

				# Results sheet
				outputfile.write("\\newline\n\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\centering\n\\begin{tabular}{|M{4cm}|M{10cm}|}\n\n\n\hline\nLatency & \\\\[50pt] \n\hline \nRange & \\\\[50pt] \n\hline \n\nBattery Life & \\\\[50pt] \n\hline \nRemarks & \\\\[50pt] \n\hline \nImprovements & \\\\[50pt] \n\hline \n\end{tabular}\n");
										
				with open('testfooterT2.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
	x=0;


	outputfile.write("\chapter{Category 3}\n");
	for row in testslist:
		x=x+1;
		if len(row) > 0:
			value = testslist[x-1][0];
			number_of_people = testslist[x-1][1];
			who = testslist[x-1][2];
			action = testslist[x-1][3];
			does_what = testslist[x-1][4];
			needed_devices = testslist[x-1][5];
			mesh_extender = testslist[x-1][6];
			when = testslist[x-1][7];
			where = testslist[x-1][8];
			specifics = testslist[x-1][9];
			user_interface = testslist[x-1][10];
			expected_result = testslist[x-1][11];
			s=str(value);	
			if s[:2]=="T3":
				outputfile.write("\section{Test ID : "+s+"}\n");
				with open('testheaderT3.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
				# Writing the test needs
				outputfile.write("Test ID : "+s+"\n This test aims at testing the "+action+" functions of the Serval Software, using "+needed_devices+" with "+specifics+" specifics, in "+where+".\n");
				# Writing the subsection for equipment needed
				outputfile.write("\subsection{Equipment needed} To realise this test, you will need:\n\\begin{itemize}\n\item "+needed_devices+" ;\n\item "+specifics+" specifics;\n\item "+mesh_extender+" mesh extender(s);\n\item "+number_of_people+"\n\end{itemize}\nThis test should be realised in "+where+".\n");
				# Writing the subsection for the operational mode of the test
				# Differentiate between app and captive portal
				tool = user_interface;
				sttool = str(tool);
				if sttool[:10]=="Serval App":
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item Open the App.\n\item Connect to a ME.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the app and switch off the "+needed_devices+".\n");
				else :
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item If a browser didn't open automatically, open one.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the browser and switch off the "+needed_devices+".\n");
				# Writing the expected results and design a sheet
				outputfile.write("\subsection{Expected results} The expected results are "+expected_result+"\n\\newline");

				# Check box for expected results
				outputfile.write("\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\\renewcommand{\\arraystretch}{2.5}\n\centering\n\\begin{tabular}{|M{4cm} M{4.8cm} M{4.8cm}|}\n\n\hline\nCheck ? & $\Box$ Yes & $\Box$ No\\\\ \n\hline \n\end{tabular}\n\\newline\n");

				# Results sheet
				outputfile.write("\\newline\n\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\centering\n\\begin{tabular}{|M{4cm}|M{10cm}|}\n\n\n\hline\nLatency & \\\\[50pt] \n\hline \nRange & \\\\[50pt] \n\hline \n\nBattery Life & \\\\[50pt] \n\hline \nRemarks & \\\\[50pt] \n\hline \nImprovements & \\\\[50pt] \n\hline \n\end{tabular}\n");
				with open('testfooterT3.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);

	x=0;


	outputfile.write("\chapter{Category 4}\n");
	for row in testslist:
		x=x+1;
		if len(row) > 0:
			value = testslist[x-1][0];
			number_of_people = testslist[x-1][1];
			who = testslist[x-1][2];
			action = testslist[x-1][3];
			does_what = testslist[x-1][4];
			needed_devices = testslist[x-1][5];
			mesh_extender = testslist[x-1][6];
			when = testslist[x-1][7];
			where = testslist[x-1][8];
			specifics = testslist[x-1][9];
			user_interface = testslist[x-1][10];
			expected_result = testslist[x-1][11];
			s=str(value);	
			if s[:2]=="T4":
				outputfile.write("\section{Test ID : "+s+"}\n");
				with open('testheaderT4.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
				# Writing the test needs
				outputfile.write("Test ID : "+s+"\n This test aims at testing the "+action+" functions of the Serval Software, using "+needed_devices+" with "+specifics+" specifics, in "+where+".\n");
				# Writing the subsection for equipment needed
				outputfile.write("\subsection{Equipment needed} To realise this test, you will need:\n\\begin{itemize}\n\item "+needed_devices+" ;\n\item "+specifics+" specifics;\n\item "+mesh_extender+" mesh extender(s);\n\item "+number_of_people+"\n\end{itemize}\nThis test should be realised in "+where+".\n");
				# Writing the subsection for the operational mode of the test
				# Differentiate between app and captive portal
				tool = user_interface;
				sttool = str(tool);
				if sttool[:10]=="Serval App":
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item Open the App.\n\item Connect to a ME.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the app and switch off the "+needed_devices+".\n");
				else :
					outputfile.write("\subsection{Operational mode} \\begin{itemize}\n\item Put the Mesh Extender at the defined spot.\n\item Turn on the ME.\n\item Connect the "+needed_devices+" to the \emph{public.servalproject.org} Wi-Fi network.\n\item If a browser didn't open automatically, open one.\n\item "+does_what+".\n\end{itemize}\nOnce you have noted the results, close the browser and switch off the "+needed_devices+".\n");
				# Writing the expected results and design a sheet
				outputfile.write("\subsection{Expected results} The expected results are "+expected_result+"\n\\newline");

				# Check box for expected results
				outputfile.write("\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\\renewcommand{\\arraystretch}{2.5}\n\centering\n\\begin{tabular}{|M{4cm} M{4.8cm} M{4.8cm}|}\n\n\hline\nCheck ? & $\Box$ Yes & $\Box$ No\\\\ \n\hline \n\end{tabular}\n\\newline\n");

				# Results sheet
				outputfile.write("\\newline\n\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n\centering\n\\begin{tabular}{|M{4cm}|M{10cm}|}\n\n\n\hline\nLatency & \\\\[50pt] \n\hline \nRange & \\\\[50pt] \n\hline \n\nBattery Life & \\\\[50pt] \n\hline \nRemarks & \\\\[50pt] \n\hline \nImprovements & \\\\[50pt] \n\hline \n\end{tabular}\n");
				with open('testfooterT4.tex','r') as infile:
					data=infile.read();
					outputfile.write(data);
	x=0;

# Write document footer

with open('docfooter.tex', 'r') as infile:
	data=infile.read().replace('\n', '')
	outputfile.write(data);

