from django import forms
import pickle


#class ListForm(forms.Form):
#        List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
#                                             choices=result_query())
#        def result_query(self):
#            pickle_off = open("title_to_surface_names_with_uid.pickle","rb")
#            new_dict = pickle.load(pickle_off)
            # you can use that with self if u need transfers.pk for querying
#            return (new_dict[var])
