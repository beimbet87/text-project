from django.shortcuts import render
from .forms import TextInputForm
from django.shortcuts import redirect
import re

def text_input_view(request):
    endings = ['ция', 'сив']
    if request.method == 'POST':
        form = TextInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Reading from text area
            manual_text = form.cleaned_data.get('text_area')

            # Reading from file if uploaded
            uploaded_file = form.cleaned_data.get('text_file')
            file_text = ""
            if uploaded_file:
                file_text = uploaded_file.read().decode('utf-8')

            # Combine text or handle separately
            combined_text = manual_text + file_text

            terms = extract_terms_with_endings_from_file(endings, file_text)

            return render(request, 'result.html', {'text': terms})

    else:
        form = TextInputForm()

    return render(request, 'form.html', {'form': form})

def extract_terms_with_endings_from_file(endings, text):
    
    # Remove punctuation using regex and split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Filter words that end with any of the given endings
    term_words = [word for word in words if any(word.endswith(ending) for ending in endings)]
    
    return term_words

def home(request):
    return redirect('text_input')