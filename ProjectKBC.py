questions = {"Which country is known as the “Land of the Rising Sun”? A- China B- Japan C- Thailand D- Korea": "B",
             "What is the square root of 144? A: 10 B: 11 C: 12 D: 13":"C",
             "Which of these is a primary colour? A: Red B: Green C: Black D: White": "A",
             "What is the capital of India? A: Mumbai B: New Delhi C: Kolkata D: Chennai": "B",
             "Who is known as the 'Father of the Nation' in India? A: Jawaharlal Nehru B: Mahatma Gandhi C: Sardar Patel D: Bhagat Singh": "B",
             "Which device is used to measure temperature? A: Thermometer B: Barometer C: Hygrometer D: Altimeter": "A",
             "Who is the host of KBC (as of recent seasons)? A: Salman Khan B: Amitabh Bachchan C: Shahrukh Khan D: Aamir Khan": "B",
             "Which animal is known as the 'Ship of the Desert'? A: Horse B: Camel C: Donkey D: Mule": "B",
             "Which festival is known as the 'Festival of Lights'? A: Holi B: Diwali C: Eid D: Christmas": "B",
             "In cricket, how many runs are scored for hitting the ball over the boundary without bouncing? A: 4 B: 6 C: 5 D: 2": "B",
             "What is the currency of Japan? A: Yen B: Yuan C: Dollar D: Won": "A",
             "Who wrote the national anthem of India? A: Bankim Chandra Chattopadhyay B: Rabindranath Tagore C: Sarojini Naidu D: Subramania Bharati": "B",
             "Which Mughal emperor built the Taj Mahal? A: Akbar B: Shah Jahan C: Aurangzeb D: Jahangir": "B",
             "Which is the smallest state in India by area? A: Goa B: Sikkim C: Tripura D: Mizoram": "A",
             "In which year did India gain independence? A: 1945 B: 1947 C: 1950 D: 1952": "B",
             "The word 'Satyameva Jayate' is taken from which ancient scripture? A: Rigveda B: Mundaka Upanishad C: Mahabharata D: Ramayana": "B",
             "Which city is known as the 'Pink City' of India? A: Jaipur B: Jodhpur C: Udaipur D: Bikaner": "A",
             "Who was the first woman Prime Minister of India? A: Indira Gandhi B: Sarojini Naidu C: Sonia Gandhi D: Pratibha Patil": "A",
             "In which state is the Sun Temple of Konark located? A: Odisha B: Gujarat C: Rajasthan D: Karnataka": "A",
             "What does CPU stand for in computers? A: Central Process Unit B: Central Processing Unit C: Computer Processing Unit D: Central Program Unit": "B",
             "Which of these is not a programming language? A: Python B: Java C: HTML D: C++": "C",
             "Which Indian freedom fighter was known as 'Netaji'? A: Lala Lajpat Rai B: Bhagat Singh C: Subhas Chandra Bose D: Bal Gangadhar Tilak": "C",
             "In which year did the Indian Space Research Organisation (ISRO) launch Chandrayaan-1? A: 2005 B: 2008 C: 2010 D: 2013": "B",
             "Which Indian mathematician is known for his work on infinite series and number theory? A: Aryabhata B: Ramanujan C: C.V. Raman D: Harish-Chandra": "B",}
i=1
for q, a in questions.items():
     print(f"Question",i, f"is {q}")
     b = input("Type A,B,C,D").upper()
     if b!="A" and b!="B" and b!="C" and b!="D":
      print("Wrong input")
      continue
     if b==a:
      print("Correct")
      i=i+1
     else:
      print("Wrong")
      i=i+1
      break
     if i > 15:
        print("COngratulations You are A Millionaire")
        break
c = i-2
Money = {0:"Nothing lmao",
         1:1000,
         2:2000,
         3:3000,
         4:5000,
         5:10000,
         6:20000,
         7:40000,
         8:80000,
         9:160000,
         10:320000,
         11:640000,
         12:1250000,
         13:2500000,
         14:5000000,
         15:70000000,}
print(f"Congratulations you won {Money[c]} Rupees")
print("Thanks for playing")
feat: add main game script
