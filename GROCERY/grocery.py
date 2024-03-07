import sqlite3

groceries = [
    "உளுத்தம் பருப்பு - Urad Dal",
    "பாசி பருப்பு - Moong Dal",
   "துவரம் பருப்பு - Toor Dal",
   "கொண்டைக்கடலை - Chickpeas",
   "கடலை பருப்பு - Bengal Gram",
   "பச்சை பட்டாணி - Green Peas",
   "மைசூர் பருப்பு - Masoor Dal",
   "முழு உளுந்து - Black Gram",
   "முழு துவரை - Whole Toor Dal",
   "சோயா பீன்ஸ் - Soya beans",
   "நிலக்கடலை - Groundnut",
   "பொட்டு கடலை  - Roasted Gram",

   "பச்சரிசி - Raw Rice",
   "புழுங்கல் அரிசி - Boiled Rice",
   "இட்லி அரிசி - Idli Rice",
   "பாஸ்மதி அரிசி - Basmati Rice",   
   "சிகப்பரிசி - Red Rice",
   "கவுனி அரிசி - Gouni Rice",
   "பிரவுன் அரிசி - Brown Rice",
   "சூரியகாந்தி எண்ணெய் - Sunflower oil",
   "கடலை எண்ணெய் - Groundnut Oil",
   "நல்லெண்ணெய் - Gingelly Oil",
   "தேங்காய் எண்ணெய் - Coconut Oil",
   "ஆலிவ் ஆயில் - Olive Oil",
   "நெய் - Ghee",
   "வனஸ்பதி - Dalda",

   "உப்பு - Salt",
   "கல் உப்பு - Crystal Salt",
   "வெல்லம் - Jaggery",
   "பனை வெல்லம் - Palm Jaggery",
   "டீத்தூள் - Tea",
   "காபி தூள் - Coffee Powder"
   "புளி - Tamarind",
   "பெருங்காயம் கட்டி அல்லது தூள் -  Asafoetida",
   "வர மிளகாய் - Chilly",
   "கடுகு - Mustard",
   "சீரகம் - Cumin",
   "வெந்தயம் - Fenugreek",
   "பெருஞ்சீரகம் / சோம்பு - Fennel",
   "மிளகு - Pepper",  
   "கசகசா - Poppy Seeds",  
   "எள் (கருப்பு அல்லது வெள்ளை) - Sesame Seeds",
   "ஓமம் - Ajwain / Carom Seeds",
   "சுக்கு - Dry Ginger",
   "ஏலக்காய் - Cardamom",
   "பட்டை  - Cinnamon",
   "கிராம்பு - Clove",
   "பிரியாணி இலை - Bay Leaf",
   "அப்பளம் அல்லது வடகம் - Pappadam",
   "ஊறுகாய் - Pickles",
   "இஞ்சி பூண்டு பேஸ்ட் - Ginger and Garlic Paste",
   "மஞ்சள் தூள்   - Turmeric Powder",
   "சாம்பார் தூள் - Sambar Powder",
   "சிக்கன் மசாலா - Chicken Spice",
   "மிளகாய் தூள் - Chilly Powder", 
   "மல்லி தூள் - Coriander Powder",
   "கரம் மசாலா தூள் - Garam Masala Powder",
   "மிளகு தூள் - Pepper Powder",
   "சீரகம் தூள் - Cumin Powder",
   "இட்லி பொடி- Idly Powder",
   "பூண்டு பொடி- Garlic Powder",
   "ரசப்பொடி  - Rasam Powder",
    "வத்தக்குழம்பு  பேஸ்ட் - Vatha Kulambu Paste",
    "சென்னா மசாலா பொடி - Chana Masala Powder",
   "சோயா சாஸ் - Soy Sauce"
   "தக்காளி கெட்ச்அப் - Tomato Ketchup"
   "சில்லி சாஸ் - Chili Sauce",
   "வினிகர் - Vinegar",
   "மயோனைஸ் - Mayonnaise",
   "ஜாம் - Jam",
   "சீஸ் - Cheese",
   "வெண்ணெய் - Butter",
   "பன்னீர் - Paneer"
  "பிரஷ் கிரீம் - Fresh Cream"
    "தேன் - Honey",
    "கோதுமை மாவு - Wheat Flour",
  "மைதா மாவு - Refined Wheat Flour",
    "ராகி மாவு - Finger Millet Flour",
   "அரிசி மாவு - Rice Flour",
   "ரவை - Suji/ Semolina",
   "ராகி - Finger Millet",
   "பாஸ்தா - Pasta",
   "நூடுல்ஸ் - Noodles",
   "அவல் - Flattened Rice",
   "ஜவ்வரிசி - Sago",
    "கடலை மாவு - Gram Flour",
   "சேமியா - Vermicelli",
   "சம்பா கோதுமை - Samba Wheat",
   "சோளம் - Maize",
  "தினை - Millet",
  "குதிரை வாலி - Barnyard Millet",

]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
	cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()