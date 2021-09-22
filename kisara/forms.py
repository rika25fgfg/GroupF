from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label= "お名前", max_length=30)
    email = forms.EmailField(label="メールアドレス")
    title = forms.CharField(label="タイトル", max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
    
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']