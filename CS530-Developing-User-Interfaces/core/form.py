from django import forms


class ImageUploadForm(forms.Form):
    art_image = forms.ImageField()


class VideoUploadForm(forms.Form):
    art_video = forms.FileField()


class ImageUploadFormProduct(forms.Form):
    thumb = forms.ImageField()
    img1 = forms.ImageField()
    img2 = forms.ImageField()
    img3 = forms.ImageField()
    img4 = forms.ImageField()
    img5 = forms.ImageField()


class FileUpload1(forms.Form):
    excel = forms.FileField()
