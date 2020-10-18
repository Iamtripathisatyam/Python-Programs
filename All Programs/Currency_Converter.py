# X-Rates.com
with open('currency.txt') as f:
    a=f.readlines()
dict={}
for i in a:
    parsed=i.split("\t")
    dict[parsed[0]]=parsed[1]
cur=int(input("\nPlease Enter the Amount : \n"))
[print(item) for item in dict.keys()]
nam=input("\n\nNow !! Please enter the name of the currency you want to CONVERT to : ")
print(f"{cur} INR is equal to : {cur*float(dict[nam])} {nam}")






Argentine Peso	0.960604	1.041012
Australian Dollar	0.018741	53.357851
Bahraini Dinar	0.005035	198.608715
Botswana Pula	0.154583	6.469012
Brazilian Real	0.069242	14.442175
British Pound	0.010530	94.964925
Bruneian Dollar	0.018527	53.976557
Bulgarian Lev	0.022720	44.014332
Canadian Dollar	0.018012	55.519761
Chilean Peso	10.333140	0.096776
Chinese Yuan Renminbi	0.093400	10.706607
Colombian Peso	48.510061	0.020614
Croatian Kuna	0.087412	11.440083
Czech Koruna	0.305668	3.271527
Danish Krone	0.086463	11.565603
Emirati Dirham	0.049179	20.334071
Euro	0.011616	86.084551
Hong Kong Dollar	0.103798	9.634079
Hungarian Forint	4.064938	0.246006
Icelandic Krona	1.836662	0.544466
Indonesian Rupiah	196.263364	0.005095
Iranian Rial	562.684142	0.001777
Israeli Shekel	0.045765	21.850870
Japanese Yen	1.430770	0.698925
Kazakhstani Tenge	5.521527	0.181109
Kuwaiti Dinar	0.004107	243.490854
Libyan Dinar	0.018637	53.656753
Malaysian Ringgit	0.056948	17.559841
Mauritian Rupee	0.537102	1.861845
Mexican Peso	0.298613	3.348817
Nepalese Rupee	1.607500	0.622084
New Zealand Dollar	0.020117	49.709955
Norwegian Krone	0.121935	8.201064
Omani Rial	0.005149	194.218145
Pakistani Rupee	2.252194	0.444011
Philippine Peso	0.661099	1.512632
Polish Zloty	0.051454	19.434826
Qatari Riyal	0.048743	20.515625
Romanian New Leu	0.056224	17.785983
Russian Ruble	0.947747	1.055133
Saudi Arabian Riyal	0.050216	19.913834
Singapore Dollar	0.018527	53.976557
South African Rand	0.219887	4.547789
South Korean Won	15.990299	0.062538
Sri Lankan Rupee	2.487850	0.401954
Swedish Krona	0.118894	8.410860
Swiss Franc	0.012485	80.096588
Taiwan New Dollar	0.393748	2.539693
Thai Baht	0.423381	2.361942
Trinidadian Dollar	0.090506	11.049038
Turkish Lira	0.091692	10.906133
US Dollar	0.013391	74.676877
Venezuelan Bolivar	0.133743	7.477034Jul 22, 2020 06:19 UTC
