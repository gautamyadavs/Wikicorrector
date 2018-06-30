import re, pickle, os, bz2
from string import ascii_lowercase


all = "static/extract/"
flag = 1
pickle_off = open("static/title_to_surface_names_with_uid.pickle","rb")
new_dict = pickle.load(pickle_off)
#new_dict = sorted(dict.items(), key=lambda s: s[0])

for i in ascii_lowercase:
    directory = os.path.dirname(all+i+'/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(all+i+'/data.pickle'):
        data = {}
        with open(all+i+'/data.pickle', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

for i in range(10):
    directory = os.path.dirname(all+str(i)+'/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(all+str(i)+'/data.pickle'):
        data = {}
        with open(all+str(i)+'/data.pickle', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

for n in new_dict.keys():
    print(n+" writing at "+n[0].lower()+"/ folder")
    with open(all+n[0].lower()+'/data.pickle', 'wb') as f:
        example_dict = {}
        example_dict[n] = new_dict[n]
        pickle_out = open(all+n[0].lower()+'/data.pickle',"wb")
        pickle.dump(example_dict, pickle_out)
        pickle_out.close()
