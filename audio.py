import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# List available voices to select a female voice
voices = engine.getProperty('voices')

# Choose a female voice (this depends on your system, typically female voices have an ID like 1 or higher)
for voice in voices:
    if "female" in voice.name.lower():  # Selects the female voice if available
        engine.setProperty('voice', voice.id)
        break

# Set properties (optional)
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1)    # Volume (0.0 to 1.0)

# The text to convert to audio
text =" Plant name is Ashwagandh( Withania somnifera) or  ginseng or winter cherry.     Disease                 It reduces stress, boosts energy, supports immunity, improves fertility, balances hormones, and enhances cognitive function .  Advantage              Ashwagandha is an adaptogenic herb that helps reduce stress, anxiety, and cortisol levels, promoting overall relaxation. It boosts energy, stamina, and muscle strength, while supporting cognitive function and memory. Ashwagandha also enhances immunity, balances hormones, and promotes restful sleep. With its anti-inflammatory properties, it improves physical resilience and is often used as a general health tonic for overall well-being.   Disadvantage            Ashwagandha is not suitable for everyone. Pregnant and breastfeeding women should avoid it as it may cause complications or premature birth. People with autoimmune diseases like rheumatoid arthritis, lupus, or multiple sclerosis should be cautious, as it can stimulate the immune system. Those with hyperthyroidism should avoid it due to its potential to increase thyroid hormone levels. Individuals on medications for sedation, thyroid disorders, or immunosuppression should also avoid Ashwagandha, as it may interact with these drugs. Additionally, people with stomach ulcers should refrain from using Ashwagandha, as it can irritate the gastrointestinal tract. Traditional uses is    Traditionally, Ashwagandha has been a key herb in Ayurvedic medicine for over 3,000 years, primarily used to rejuvenate and restore energy. It is regarded as a Rasayana in Ayurveda, meaning it promotes longevity, vitality, and overall well-being. Ashwagandha has been used to enhance physical and mental stamina, support the immune system, and improve sexual health and fertility in both men and women. It has also been used to strengthen muscles, improve cognitive function, and support healthy aging, especially in the elderly. Traditionally, Ashwagandha is consumed in the form of powders, teas, or tonics, often mixed with milk or honey."
        
# Save the speech to an audio file
audio_file_path = r'C:\Users\NITINSIR\Desktop\Herb Mitra\audio_file.mp3'
engine.save_to_file(text, audio_file_path)

# Run the speech engine to process the audio
engine.runAndWait()

# Output the path to the generated audio file
audio_file_path
