from flask import Flask, render_template, request, redirect, url_for
import openai
import os
import logging

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
    if request.method == 'POST':
        social_media = request.form.getlist('social_media')
        research_text = request.form['research_text']
        
        research_text = " ".join(research_text.splitlines())  # Удаление пустых строк
        
        summarized_text = summarize_research_text(research_text)
        
        truncated_text = research_text
        

        posts = {}  # Словарь для хранения постов для каждой социальной сети

        #if 'twitter' in social_media:
           
        rule_tw = "Create an engaging Twitter post, within 340 characters, that includes a call to action to encourage readers to follow the study. Don't forget to include a clickable link. Additionally, please include the following hashtags for the studies: #VisualAbstract, #GraphicalAbstract, #Sciencecommunication "
        research_text_tw = rule_tw + truncated_text
        print(research_text_tw)
        summarized_text_tw = summarize_research_text(research_text_tw)
        twitter_post = summarized_text_tw
        posts['twitter_post'] = twitter_post 
        #if 'linkedin' in social_media:
        
        rule_li = "Create an attention-grabbing LinkedIn post with a catchy headline, limited to 140 characters, followed by an introduction of the research text. Ensure that the post does not include any hashtags. You can also include 4-5 emojis within the post. The overall character limit for the post is 1000 characters"
        rule_li1 ="Want to learn more? 🤔 Follow the link and discover the full findings of our research on concussions and their economic effects. #concussionresearch #economicimpact #publichealth #braininjury #VisualAbstract #GraphicalAbstract #Sciencecommunication"
        research_text_li = rule_li + truncated_text 
        summarized_text_li = summarize_research_text(research_text_li)
        linkedin_post = summarized_text_li + rule_li1
        posts['linkedin_post'] = linkedin_post
            
#if 'instagram' in social_media:
        rule_inst = "Interested in more details about the study? Click on the link in our Story/Highlights #concussionresearch #economicimpact #publichealth #braininjury #VisualAbstract #GraphicalAbstract #Sciencecommunication "
        research_text_inst =  summarized_text_li + rule_inst
        summarized_text_inst = research_text_inst
        instagram_post = summarized_text_inst 
        posts['instagram_post'] = instagram_post
        form1_class = "form1"
            

        #return render_template('index.html', **posts)
        return render_template('index.html', twitter_post=twitter_post, linkedin_post=linkedin_post, 
                       instagram_post=instagram_post, form1_class=form1_class,display_property='block')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    app.run(debug=True)