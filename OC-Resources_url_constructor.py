import pandas as pd

def load_parse(file):
   f = open(file, 'r')
   f_lines = f.readlines()
   list_of_lists = []
   for line in f_lines:
       tmp_line = line.split()
       list_of_lists.append(tmp_line)

   df = pd.DataFrame(data=list_of_lists)
   new_header = df.iloc[0]  
   df = df[1:] 
   df.columns = new_header  
   df = df.reset_index() 
   for index, row in df.iterrows():
       if row['NAMESPACED'] == "true" or row['NAMESPACED'] == "false":
           continue
       tmp_vale = row['SHORTNAMES']
       tmp_vale_2 = row['APIVERSION']
       tmp_vale_3 = row['NAMESPACED']
       df.at[index,'KIND'] = tmp_vale_3
       df.at[index, 'NAMESPACED'] = tmp_vale_2
       df.at[index, 'APIVERSION'] = tmp_vale
       df.at[index, 'SHORTNAMES'] = ''

   return df

def constract_url(df):
   host = "host" # edit host here
   url = ''
   urls = []
   df = df.reset_index()  # make sure indexes pair with number of rows
   for index, row in df.iterrows():
       if (row['NAMESPACED'] == 'true'):
           address_touple = (host, row['APIVERSION'], namespace, row['NAME'])
           url = "/".join(address_touple)
           print(url)
           urls.append(url)
       else:
           address_touple = (host, row['APIVERSION'], row['NAME'])
           url = "/".join(address_touple)
           print(url)
           urls.append(url)
   return urls





if __name__ == '__main__':
   print("started parsing")
   df = load_parse("oc-output.txt") # edit the ouput.txt 
   out = open('out-apis', 'w')
   urls = constract_url(df)
   print("the urls:\n")
   print(urls)
   for url in urls:
       out.writelines(url)
       out.writelines('\n')
   out.close()
