from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

openai.api_key = "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"

def summarize_research_text(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None
    )
    summarized_text = response.choices[0].text.strip()
    return summarized_text

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    '''if request.method == 'POST':
        social_media = request.form['social_media']
        if social_media == 'about':
            return redirect(url_for('about'))
        else:
            research_text = request.form['research_text']
            if social_media == 'twitter':
                summarized_text = summarize_research_text(research_text)
                truncated_text = summarized_text[:1000]
                twitter_post = f"{truncated_text}"
                return render_template('index.html', twitter_post=twitter_post)
            elif social_media == 'linkedin':
                summarized_text = summarize_research_text(research_text)
                truncated_text = summarized_text[:1000]
                headline = truncated_text[:140]
                linkedin_post = f"{headline}\n\n{truncated_text}"
                return render_template('index.html', linkedin_post=linkedin_post)
            elif social_media == 'instagram':
                summarized_text = summarize_research_text(research_text)
                truncated_text = summarized_text[:1000]
                starting_part = truncated_text[:120]
                instagram_post = f"{starting_part}\n\n{truncated_text}"
                return render_template('index.html', instagram_post=instagram_post)
    
    return render_template('index.html')'''
    if request.method == 'POST':
        social_media = request.form['social_media']
        if social_media == 'about':
            return redirect(url_for('about'))
        else:
            research_text = request.form['research_text']
            if social_media in ['twitter', 'linkedin', 'instagram']:
                summarized_text = summarize_research_text(research_text)
                truncated_text = summarized_text[:1000]
                
                if social_media == 'twitter':
                    twitter_post = f"{truncated_text}"
                    return render_template('index.html', twitter_post=twitter_post)
                elif social_media == 'linkedin':
                    headline = truncated_text[:140]
                    linkedin_post = f"{headline}\n\n{truncated_text}"
                    return render_template('index.html', linkedin_post=linkedin_post)
                elif social_media == 'instagram':
                    starting_part = truncated_text[:120]
                    instagram_post = f"{starting_part}\n\n{truncated_text}"
                    return render_template('index.html', instagram_post=instagram_post)
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
