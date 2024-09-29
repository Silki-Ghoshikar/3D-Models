from pymongo import MongoClient, errors

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Change the URI if using a cloud service

# Create or switch to the database
db = client['PlantDatabase']

# Create or switch to the collection
collection = db['PlantInfo']

# Create a unique index on the Plant_name field
try:
    collection.create_index([('Plant_name', 1)], unique=True)
    print("Unique index on 'Plant_name' created.")
except errors.OperationFailure as e:
    print(f"Index creation failed: {e}")

# Sample document to insert
sample_data = {
    "Plant_name": "Aloe Vera (Aloe barbadensis miller), ",
    "Disease": "Aloe vera juice may help relieve constipation it is sometimes used for soothing symptoms of irritable bowel syndrome (IBS),also Sunburn relief , Acne treatment ,Soothing dry or irritated skin",
    "Advantage": "Natural Remedy: Aloe vera offers a natural option for skin care and minor health issues, avoiding the need for synthetic products. Versatility: Aloe vera can be used in various forms—fresh gel, juices, creams, and ointments—making it versatile for different applications.  Low Mainteance: The plant is relatively easy to grow and care for, requiring minimal water and light conditions. Aloe vera can be used in toothpaste or mouthwash for gum health and reducing plaque.",
    "Disadvantage": "Allergic Reactions: Some individuals may experience allergic reactions or skin irritation when using aloe vera. It’s recommended to do a patch test before using it extensively. Laxative Effect: Aloe vera latex, which is a yellowish substance found under the skin of the leaves, has a strong laxative effect and can cause gastrointestinal issues if ingested. Contamination Risk: Aloe vera products can sometimes be contaminated with other substances or contain added chemicals, so it’s important to choose high-quality, pure products. Limited Efficacy: While aloe vera has many anecdotal benefits, scientific evidence supporting some of its claims, particularly for internal use, can be limited.",
    "Traditional_use": "Medicinal Uses: Aloe vera has been used traditionally to treat minor burns, cuts, and abrasions. It is also used to soothe irritated skin and reduce inflammation.  Digestive Health: In traditional medicine, aloe vera juice is sometimes used to aid digestion and relieve constipation, though its effectiveness can vary. Cosmetic Applications: Aloe vera is a common ingredient in skincare and haircare products due to its moisturizing and soothing properties.",
    "Audio": "Aloe Vera.mp3",  # replace with actual audio link
    "3D_model": "aloe_vera_plant (2).glb"  # updated to GLB format
}

# Sample data to insert (list of dictionaries)
new_data = [
    {
        "Plant_name": "Dandelion",
        "Disease": "It can cause allergic reactions, digestive issues like diarrhea, dehydration from its diuretic effect, and may affect blood sugar levels. While it doesn't directly cause diseases, these adverse effects can occur in sensitive individuals.",
        "Advantage": "Dandelion is highly beneficial for health, supporting digestion, liver function, and acting as a natural diuretic to reduce water retention. It's rich in vitamins and antioxidants, helping fight inflammation. Additionally, it's versatile in cooking, with its leaves, roots, and flowers used in salads, teas, and more, making it a valuable plant for both nutrition and wellness.",
        "Disadvantage": "Dandelion can cause allergic reactions, dehydration due to its diuretic effect, and may interact with medications. Its bitter taste may be unappealing, and excessive consumption can lead to digestive issues. Moderation and caution are advised, especially if on medication.",
        "Traditional_use": "Dandelion has been traditionally used for its medicinal and culinary benefits. It supports digestion, liver health, and acts as a natural diuretic. The leaves are eaten in salads, the roots roasted for coffee, and the flowers used to make wine. Additionally, it is used in folk remedies for skin issues and inflammation, making it a versatile plant in traditional healing practices.",
        "Audio": "dailalimin.mp3",  # replace with actual audio link
        "3D_model": "dandelion_blossom_flower_game_ready_asset.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Neem",
        "Disease": "Neem is beneficial for various health conditions, including skin issues like acne and eczema, dental health, and digestive disorders. It helps regulate blood sugar for diabetes, fights infections with its antimicrobial properties, and supports blood purification. Additionally, neem boosts the immune system and reduces inflammation, making it valuable in traditional medicine.",
        "Advantage": "Neem offers several health benefits, including antimicrobial properties that combat infections and skin benefits for conditions like acne and eczema. It purifies the blood and boosts the immune system while promoting digestive health and preventing gum disease. Additionally, neem oil acts as a natural insect repellent and pesticide, making it a valuable resource in traditional and modern medicine.",
        "Disadvantage": "It including potential allergic reactions in sensitive individuals, such as skin rashes or irritation. Excessive consumption can lead to digestive issues like nausea or diarrhea. It may also lower blood sugar levels, posing a risk for people with diabetes if not monitored. Additionally, neem oil can be toxic if ingested in large quantities, and its bitter taste may be unpalatable for some. Care should be taken, especially when using neem products in large amounts or by those with existing health conditions.",
        "Traditional_use": " Its leaves purify blood and boost immunity, while neem oil treats skin issues like acne and eczema. The bark is used in teas for digestion and oral health. Additionally, neem balances doshas in Ayurveda and serves as a natural insect repellent, making it a vital part of traditional medicine.",
        "Audio": "neem.mp3",  # replace with actual audio link
        "3D_model": "neem_tree (1).glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Ginger (*Zingiber officinale*)",
        "Disease": "Ginger (*Zingiber officinale*) is generally safe but can cause issues in some individuals. It may lead to gastrointestinal upset, stimulate bile production (worsening gallbladder conditions), and increase bleeding risk due to its blood-thinning properties. Pregnant women should be cautious as excessive ginger may raise miscarriage risks. It can also lower blood sugar levels, which might affect those with diabetes. Additionally, some may experience allergic reactions. It's advisable to consult a healthcare professional before consuming large amounts of ginger, especially for those with specific health concerns.",
        "Advantage": "Ginger offers several health advantages, including promoting digestive health by alleviating nausea and bloating, providing anti-inflammatory effects to reduce pain from conditions like arthritis, and relieving cold and flu symptoms. It serves as a natural pain reliever for headaches and menstrual cramps while boosting immune function and circulation. Additionally, ginger is rich in antioxidants, enhances the flavor of various dishes, and may aid in weight management by promoting fullness and boosting metabolism. Overall, incorporating ginger into your diet can enhance health and flavor.",
        "Disadvantage": "May cause heartburn in sensitive individuals",
        "Traditional_use": "Ginger (*Zingiber officinale*) has a long history of traditional use, primarily as a digestive aid to relieve nausea, bloating, and indigestion. It possesses anti-inflammatory properties, making it useful for arthritis and muscle pain. Additionally, ginger is commonly used to alleviate cold and flu symptoms, soothe sore throats, and provide natural pain relief for headaches and menstrual discomfort. Known for its immune-boosting effects, it is often included in tonics and teas. Beyond medicinal purposes, ginger adds flavor to various dishes and is popular in aromatherapy for its warming effects.",
        "Audio": "Ginger.mp3",  # replace with actual audio link
        "3D_model": "red_ginger.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Tulsi(Ocimum sanctum )",
        "Disease": "Tulsi is used to treat respiratory issues like asthma, bronchitis, and colds. It is also effective in managing digestive issues, stress, and skin problems. Tulsi is known for its ability to reduce fevers, fight infections, and aid in detoxification. It is frequently used in home remedies for minor ailments, including coughs, headaches, and sore throats.",
        "Advantage": "Tulsi is revered for its powerful adaptogenic and medicinal properties. It is known to boost immunity, reduce stress, and improve respiratory health. The herb acts as a natural detoxifier, supports cardiovascular health, and helps maintain blood sugar balance. It also has antioxidant, anti-inflammatory, and antimicrobial properties.",
        "Disadvantage": "Who should not use While generally safe for most people, pregnant or breastfeeding women should use Tulsi with caution, as it may have uterine-stimulating effects. Additionally, people taking blood-thinning medications or those with hypoglycemia should consult their doctor before using Tulsi, as it may interfere with these conditions.",
        "Traditional_use": "= In Ayurveda,     Tulsi is used for balancing Vata and Kapha doshas. It is traditionally used in teas, tinctures, and powders for its wide range of health benefits. Tulsi has been used for centuries to treat common colds, flu, respiratory infections, and skin conditions. Its spiritual significance involves placing Tulsi in homes for its protective and purifying energies.",
        "Audio": "tulsi.mp3",  # replace with actual audio link
        "3D_model": "tulsi.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": " Turmeric (Curcuma longa).",
        "Disease": "In terms of its therapeutic applications, turmeric is effective in managing arthritis, reducing inflammation, and improving skin conditions like eczema. It is also commonly used in wound healing, improving digestion, and regulating menstruation.",
        "Advantage": "= Turmeric is renowned for its potent anti-inflammatory and antioxidant properties, largely attributed to the active compound curcumin. It supports joint health, aids digestion, boosts immunity, and promotes overall wellness. Curcumin has also been studied for its potential to fight chronic diseases, including cancer and Alzheimer's disease.",
        "Disadvantage": "While Turmeric is safe for most people when used in food amounts, those with gallbladder problems or taking blood-thinning medications should avoid large medicinal doses. Pregnant women should also limit Turmeric intake beyond normal dietary amounts, as it may stimulate the uterus in high concentrations. ",
        "Traditional_use": "In Ayurveda, Turmeric is used to balance all three doshas (Vata, Pitta, Kapha). It is commonly consumed in the form of powder, teas, or pastes for its health benefits. Turmeric is traditionally used to purify the blood, promote healthy skin, and enhance digestive health. It is also used externally to heal wounds, reduce skin inflammation, and as a cosmetic to improve complexion.",
        "Audio": "Turmeric.mp3",  # replace with actual audio link
        "3D_model": "Turmeric_Plant.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Fennel (Foeniculum vulgare) or Saunf",
        "Disease": "Fennel is traditionally used to treat digestive disorders such as indigestion, gas, and colic in infants. It is also beneficial for respiratory conditions like asthma and bronchitis. Fennel has been used to regulate menstruation, relieve menstrual cramps, and support lactation. Additionally, it helps with weight management by curbing appetite and boosting metabolism.",
        "Advantage": "Fennel is well-known for its ability to improve digestion. It helps relieve bloating, indigestion, and flatulence. Fennel seeds contain antioxidants and anti-inflammatory compounds that support overall health. They are also known to aid in hormonal balance, improve respiratory health, and enhance lactation in nursing mothers.",
        "Disadvantage": "Despite its many benefits, fennel should be used cautiously by certain individuals. Pregnant women are advised to avoid fennel in large amounts due to its estrogenic effects, which could potentially stimulate uterine contractions. People with hormone-sensitive conditions, such as breast or ovarian cancer, should also avoid consuming large amounts of fennel due to its estrogen-like activity.",
        "Traditional_use": "Fennel has been used in various traditional systems like Ayurveda, Unani, and European herbal medicine. In Ayurveda, it balances Vata and Pitta doshas, promoting digestion and detoxification. In Unani medicine, it is used for digestive issues and respiratory health. Fennel is also commonly chewed after meals in India to freshen the breath and support digestion.",
        "Audio": "fennel.mp3",  # replace with actual audio link
        "3D_model": "Fennel.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Henna (Lawsonia inermis), or  Mehndi ",
        "Disease": " Dandruff, skin rashes, fungal infections, hair fall, headaches.",
        "Advantage":"Soothes skin irritations, promotes hair health, relieves headaches, treats fungal infections",
        "Disadvantage": " Henna should be used cautiously by people with sensitive skin or those prone to allergic reactions, as it may cause skin irritation or rashes in some individuals. Pregnant women are advised to avoid excessive use of henna, especially in large medicinal doses, due to limited research on its safety during pregnancy.",
        "Traditional_use": " Used for body art, cooling the skin, treating hair and scalp issues, reducing inflammation",
        "Audio" : "henna.mp3",
        "3D_model": "Henna.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Thippili (Piper longum),or Long Pepper or Indian Long Pepper",
        "Disease": " Asthma, bronchitis, cough, indigestion, fever, joint pain, and colds.",
        "Advantage": "Enhances digestion, relieves respiratory issues, boosts immunity, reduces inflammation, acts as a natural detoxifier",
        "Disadvantage": " Thippili should be avoided by pregnant women, as it may stimulate uterine contractions. Individuals with gastritis, ulcers, or acid reflux should also exercise caution, as it can exacerbate these conditions. Additionally, people on blood-thinning medications should consult a healthcare provider before using Thippili, as it may increase the risk of bleeding.",
        "Traditional_use": "Used for respiratory disorders, improving digestion, treating fever, detoxifying the body, and alleviating joint pain",
        "Audio": "thillpi.mp3",  # replace with actual audio link
        "3D_model": "Thippli.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Thothuvalai (Solanum trilobatum) or Purple-fruited Pea Eggplant or Thai Nightshade",
        "Disease": "Asthma, chronic cough, sore throat, bronchitis, cold, and respiratory infections.",
        "Advantage": "Improves respiratory health, relieves cough, asthma, cold, boosts immunity, reduces inflammation",
        "Disadvantage": "Thothuvalai should be used with caution by pregnant and lactating women, as its effects during pregnancy have not been thoroughly studied. People with autoimmune disorders are also advised to consult a healthcare professional before using this herb, as it may stimulate the immune system.",
        "Traditional_use": "In Ayurveda and Siddha, Thothuvalai is regarded as a Kapha-reducing herb, making it ideal for treating respiratory congestion, cold, and asthma. The leaves of the plant are also used in preparing herbal remedies for joint pain, as they possess mild analgesic and anti-inflammatory properties",
        "Audio": "thothuvalai.mp3",  # replace with actual audio link
        "3D_model": "Thootuvalai.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Calendula (Botanical Name: Calendula officinalis) or marigold",
        "Disease": "Calendula flowers are used in herbal teas to support digestive health, reduce menstrual cramps, and stimulate bile production, improving liver function. Its mild antimicrobial properties also make it effective in treating minor infections and ulcers.",
        "Advantage": "Calendula is renowned for its ability to speed up the healing process of wounds, cuts, burns, and skin irritations.",
        "Disadvantage": "While generally safe for most people, individuals who are allergic to plants in the Asteraceae family (such as daisies, chrysanthemums, or ragweed) should avoid using calendula to prevent allergic reactions. Pregnant or breastfeeding women are also advised to avoid its use internally without medical consultation, as its effects during pregnancy are not well studied.",
        "Traditional_use": "It is traditionally applied as an ointment, tincture, or infused oil to soothe inflamed skin, reduce swelling, and promote tissue regeneration.",
        "Audio": "calendula(marigold).mp3",  # replace with actual audio link
        "3D_model": "Calendula.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Arnica (Arnica montana), or  Leopard Bane ",
        "Disease": " = One of Arnica's primary benefits is its ability to reduce swelling and bruising. It is commonly applied topically to heal bruises, sprains, muscle soreness, and joint pain, including arthritis. Arnica's anti-inflammatory compounds help reduce pain and promote faster healing.",
        "Advantage":"Reduces inflammation, alleviates pain, promotes healing of bruises, sprains, and muscle soreness, treats skin irritations. ",
        "Disadvantage": " Pregnant and breastfeeding women should avoid Arnica due to its potency and potential side effects. Arnica should not be applied on broken skin or open wounds, as it can cause irritation and toxicity when absorbed into the bloodstream. People allergic to plants in the Asteraceae family (which includes daisies, marigolds, and chrysanthemums) may also be allergic to Arnica and should avoid its use.",
        "Traditional_use": " In traditional medicine, it is also used to treat skin irritations and insect bites. Arnica is widely used in homeopathy and herbal medicine for treating physical injuries and relieving pain associated with muscle and joint conditions.",
        "Audio" : "Arnica.mp3",
        "3D_model": "arnica.glb"  # replace with actual 3D model link
    },
    {
        "Plant_name": "Ashwagandh( Withania somnifera) or  ginseng or winter cherry",
        "Disease": "It reduces stress, boosts energy, supports immunity, improves fertility, balances hormones, and enhances cognitive function",
        "Advantage":"Ashwagandha is an adaptogenic herb that helps reduce stress, anxiety, and cortisol levels, promoting overall relaxation. It boosts energy, stamina, and muscle strength, while supporting cognitive function and memory. Ashwagandha also enhances immunity, balances hormones, and promotes restful sleep. With its anti-inflammatory properties, it improves physical resilience and is often used as a general health tonic for overall well-being.",
        "Disadvantage": " Ashwagandha is not suitable for everyone. Pregnant and breastfeeding women should avoid it as it may cause complications or premature birth. People with autoimmune diseases like rheumatoid arthritis, lupus, or multiple sclerosis should be cautious, as it can stimulate the immune system. Those with hyperthyroidism should avoid it due to its potential to increase thyroid hormone levels. Individuals on medications for sedation, thyroid disorders, or immunosuppression should also avoid Ashwagandha, as it may interact with these drugs. Additionally, people with stomach ulcers should refrain from using Ashwagandha, as it can irritate the gastrointestinal tract.",
        "Traditional_use": "Traditionally, Ashwagandha has been a key herb in Ayurvedic medicine for over 3,000 years, primarily used to rejuvenate and restore energy. It is regarded as a Rasayana in Ayurveda, meaning it promotes longevity, vitality, and overall well-being. Ashwagandha has been used to enhance physical and mental stamina, support the immune system, and improve sexual health and fertility in both men and women. It has also been used to strengthen muscles, improve cognitive function, and support healthy aging, especially in the elderly. Traditionally, Ashwagandha is consumed in the form of powders, teas, or tonics, often mixed with milk or honey.",
        "Audio" : "ashwagandha.mp3",
        "3D_model": "Ashvagandha.glb"  # replace with actual 3D model link
    }
]

# Insert multiple documents at once
try:
    result = collection.insert_many(new_data)
    print(f'Documents inserted with IDs: {result.inserted_ids}')
except errors.BulkWriteError as e:
    print(f"Error inserting documents: {e.details}")

# Insert the sample document into the collection
try:
    result = collection.insert_one(sample_data)
    # Print the inserted document ID
    print(f'Document inserted with ID: {result.inserted_id}')
except errors.DuplicateKeyError:
    print(f"A document with the same Plant_name '{sample_data['Plant_name']}' already exists.")

# Optional: Retrieve and print all documents in the collection
for doc in collection.find():
    print(doc)

# Close the connection (optional)
client.close()
