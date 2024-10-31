import pandas as pd

# Table content as a string
table_content = """
| Number | Name (with Link)                                                                       | Batch | Session | Email                        | Organization                                       | Designation                             |
| ------ | -------------------------------------------------------------------------------------- | ----- | ------- | ---------------------------- | -------------------------------------------------- | --------------------------------------- |
| 01     | [Sakib Ahamed Shahon](https://www.linkedin.com/in/sakib-shahon/)                       | 13    | 2018-19 | sakib3201@gmail.com          | Incevio                                            | Software Engineer(Laravel)              |
| 02     | [Md Arafat Hossain](https://www.linkedin.com/in/md-arafat-hossain-437314173/)          | 13    | 2018-19 | arafat.hossain1802@gmail.com | WellDev                                            | Trainee Software Engineer(DevOps)       |
| 03     | [Md Rejwan Ahmed](https://www.linkedin.com/in/md-rejwan-ahmed-338121166/)              | 10    | 2015-16 | rejwancse10@gmail.com        | Nondito Soft                                       | Software Engineer(Laravel)              |
| 04     | [Fahim Abdullah](https://www.linkedin.com/in/fahim-d-abdullah/)                        | 10    | 2015-16 | fahim19dipu@gmail.com        | Medina Tech Ltd.                                   | Associate Data Engineer                 |
| 05     | [Md. Rafiul Islam](https://www.linkedin.com/in/md-rafiul-islam-9a765717a/)             | 12    | 2017-18 | rafiulislamrafi77@gmail.com  | Z. H. Shikder University of Science and Technology | Lecturer in CSE                         |
| 06     | [Muhammad Rifat](https://www.linkedin.com/in/rifat-mia/)                               | 12    | 2017-18 | hrifat450@gmail.com          | Bit Byte Technology Ltd.                           | Software Engineer(Android)              |
| 07     | [Md. Jubair Sayeed](https://www.linkedin.com/in/md-jubair-sayeed-linas/)               | 08    | 2013-14 | jubair.sayeed@gmail.com      | Bangladesh Computer Council                        | Assistant Network Engineer              |
| 08     | [Kamal Hossain Mitul](https://www.linkedin.com/in/khmitul/)                            | 09    | 2014-15 | kamalhossainmitul0@gmail.com | Bangladesh Rural Electrification Board             | Assistant General Manager(IT)           |
| 09     | [Dilshad Rafi Shajli](https://www.linkedin.com/in/shajli/)                             | 02    | 2007-08 | dilshad.shajli@gmail.com     | Fanfare Bangladesh Limited                         | Full Stack Developer                    |
| 10     | [Mostafa Shamin Yeasar](https://www.linkedin.com/in/mostafa-shamin-yeasar-8576941b1/)  | 10    | 2015-16 | shamin.apon.yeasar@gmail.com | BJIT Corp                                          | Software Engineer(iOS)                  |
| 11     | [S.M. Nadim](https://www.linkedin.com/in/smnadim21/)                                   | 08    | 2013-14 | smnadim21@gmail.com          | Binary Quest Limited                               | Software Engineer(Android)              |
| 12     | [Md Hasibur Rahman Evan](https://www.linkedin.com/in/evan-shareef/)                    | 12    | 2017-18 | evanshareef@gmail.com        | Vivasoft Limited                                   | Software Engineer(.Net)                 |
| 13     | [Md. Kawsarul Alam Shuvo](https://www.linkedin.com/in/shuvo806/)                       | 09    | 2014-15 | shuvo.official2021@gmail.com | Vivasoft Limited                                   | Software Engineer(Level 2)              |
| 14     | [Jannatul Ferdaous](https://www.linkedin.com/in/jannatul-ferdaous/)                    | 13    | 2018-19 | jfkhatun021@gmail.com        | Orion Informatics Ltd.                             | Trainee Software Engineer               |
| 15     | [Md. Kamran Hosan Raj](https://www.linkedin.com/in/md-kamran-hosan-693023261/)         | 12    | 2017-18 | mdkamranhosan98@gmail.com    | Synergy Interface Ltd.                             | Software Engineer(Laravel)              |
| 16     | [Md Aman Ullah](https://www.linkedin.com/in/amanullah1/)                               | 01    | 2006-07 | amanu092@gmail.com           | IQI Global, Selangor, Malaysia                     | Software Engineer(Laravel)              |
| 17     | [Md Abdur Rahim](https://www.linkedin.com/in/mdabdurrahimbd/)                          | 03    | 2008-09 | marahim.cseju@gmail.com      | German University Bangladesh                       | Asistant Professor and Head of CSE      |
| 18     | [Rubaya Mim](https://www.linkedin.com/in/rubayamim/)                                   | 11    | 2016-17 |                              | Bee Technology & Research Hub (BTRH)               | Software Engineer(Laravel)              |
| 19     | [Mizanur Rahaman](https://www.linkedin.com/in/engrmukul/)                              | 02    | 2007-08 | engrmukul@hotmail.com        | Talent Pro                                         | Software Engineer(Technical Lead)       |
| 20     | [Binta Ansary](https://www.linkedin.com/in/binta-ansary-6229091a8/)                    | 12    | 2017-18 | shanto.sa23@gmail.com        | SecurityMindPro, Melbourne, Australia              | Associate Cyber Security Analyst        |
| 21     | [Shahanaj Parvin](https://www.linkedin.com/in/shahanaj-parvin-931343137/)              | 03    | 2008-09 | putulcse9@gmail.com          | Binate Solutions Ltd.                              | Senior Flutter Developer                |
| 22     | [Md Rukon Mia](https://www.linkedin.com/in/md-rukon-mia-a6856615a/)                    | 09    | 2014-15 | marjkkniu2015@gmail.com      | Freelance IT Lab                                   | Information Technology Support Engineer |
| 23     | [Zahid Hasan](https://www.linkedin.com/in/zahid-hasan124/)                             | 12    | 2017-18 | zahid.jkkniu.cse@gmail.com   | Softivus                                           | Software Engineer(Laravel)              |
| 24     | [Anindita Acharjee](https://www.linkedin.com/in/anindita-acharjee-0439091a8/)          | 13    | 2018-19 | aninditamumu4928@gmail.com   | BugsBD Limited                                     | Intern in Cybersecurity                 |
| 25     | [Md Jannatul Ferdous Rahat Ibne Yousuf](https://www.linkedin.com/in/naymuzzamanakanda) | 13    | 2018-19 | jfrahat19@gmail.com          |                                                    | Software Engineer                       |
| 26     | [Rafiea Nusrat Mim](https://www.linkedin.com/in/rafiea-nusrat-mim/)                    | 13    | 2018-19 | rafieameem@gmail.com         | Technometrics Limited                              | Cyber Security Analyst                  |
| 27     | [Mahfuzur Rahman](https://www.linkedin.com/in/mahfuzur-rahman-2938901ba/)              | 13    | 2018-19 | mahfuzking555@gmail.com      | Mymensingh Engineering College(MUET)               | Lecturer in CSE                         |
| 28     | [Md. Abu Raihan](https://www.linkedin.com/in/raihancse0908/)                           | 03    | 2008-09 | raihan.cse08@gmail.com       | General Pharmaceuticals Limited                    | Information Technology Executive        |
| 29     | [Abu Bakar Siddique](https://www.linkedin.com/in/abu-bakar-siddique-jkkniu/)           |       | 0000000 |                              | SSL Wireless                                       | Cyber Security Engineer                 |
"""

# Convert the Markdown table to a DataFrame
df = pd.read_csv(pd.compat.StringIO(table_content), sep="|", skipinitialspace=True, engine='python')

# Drop the first and last columns which are empty due to the leading and trailing |
df = df.drop(columns=[''])

# Sort the DataFrame by the 'Name (with Link)' column
df_sorted = df.sort_values(by=' Name (with Link)')

# Convert the sorted DataFrame back to a Markdown table
sorted_markdown_table = df_sorted.to_markdown(index=False)

# Save the sorted table to a markdown file
file_path = "/mnt/data/sorted_table.md"
with open(file_path, "w") as file:
    file.write(sorted_markdown_table)

file_path