import tkinter as tf
from tkinter import *
from tkinter import ttk
from tkinter.ttk import*
import tkinter.messagebox
import pandas as pd
import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
city_checklist=("Faridabad","Ghaziabad","Noida","Gurgaon","Delhi"'Central Delhi07',
			'East Delhi','New Delhi','North Delhi','North East Delhi','North West Delhi','South Delhi','South West Delhi','West Delhi',"Allahabad","Kanpur","Patna","Varanasi","Raipur","Ludhiana","Amritsar","Bangalore","Agra","Gwalior","Mumbai","Meerut","Jalandhar","Lucknow","Kolkata","Guwahati","Hyderabad","Chennai","Vijayawada","Ahmedabad","Kochi","Pune","Belgaum","Dehradun","Visakhapatnam","Jabalpur","Vadodara","Jammu","Thane","Coimbatore","Nagpur","Ranchi","Jaipur","Indore","Navi Mumbai","Rajkot","Bhopal","Mysore","Udaipur","Jamshedpur","Surat","Thiruvananthapuram","Chandigarh","Tiruchirapalli","Bhubaneshwar","North Goa","South Goa","Shimla")
new_dist=[]
State={"Andhra Pradesh":"00",
"Arunachal Pradesh":"01",
"Assam":"02",
"Bihar":"03",
"Chhattisgarh":"04",
"Dadra and Nagar Haveli":"05",
"Daman and Diu":"06",
"Delhi":"07",
"Goa":"08",
"Gujarat":"09",
"Haryana":"10",
"Himachal Pradesh":"11",
"Jammu and Kashmir":"12",
"Jharkhand":"13",
"Karnataka":"14",
"Kerala":"31",
"Madhya Pradesh":"15",
"Maharashtra":"16",
"Manipur":"17",
"Meghalaya":"18",
"Mizoram":"19",
"Nagaland":"20",
"Orissa":"21",
"Pondicherry":"22",
"Punjab":"23",
"Rajasthan":"24",
"Sikkim":"25",
"Tamil Nadu":"26",
"Tripura":"27",
"Uttar Pradesh":"28",
"Uttarakhand":"30",
"West Bengal":"30"}

Cities=['Adilabad00',
			'Anantapur00',
			'Chittoor00',
			'Kakinada00',
      'Tiruchirappalli26'
			'Guntur00',
			'Hyderabad00',
			'Karimnagar00',
      'Jamshedpur13',
			'Khammam00',
			'Krishna00',
			'Kurnool00',
			'Mahbubnagar00',
			'Medak00',
			'Nalgonda00',
			'Nizamabad00',
			'Ongole00',
			'Hyderabad00',
			'Srikakulam00',
			'Nellore00',
			'Visakhapatnam00',
			'Vizianagaram00',
			'Warangal00',
			'Eluru00',
			'Kadapa00','Birbhum30',
			'Bankura30',
			'Bardhaman30',
			'Darjeeling30',
			'Dakshin Dinajpur30',
			'Hooghly30',
			'Howrah30',
			'Jalpaiguri30',
			'Cooch Behar30',
			'Kolkata30',
			'Maldah30',
			'Paschim Medinipur30',
			'Purba Medinipur30',
			'Murshidabad30',
			'Nadia30',
			'North 24 Parganas30',
			'South 24 Parganas30',
			'Purulia30',
			'Uttar Dinajpur30',
      'Anjaw01',
			'Changlang01',
			'East Siang01',
      'Guwahati02',
			'Kurung Kumey01',
			'Lohit01',
			'Lower Dibang Valley01',
			'Lower Subansiri01',
			'Papum Pare01',
			'Tawang01',
			'Tirap01',
			'Dibang Valley01',
			'Upper Siang01',
			'Upper Subansiri01',
			'West Kameng01',
			'West Siang01','Almora29',
			'Bageshwar29',
			'Chamoli29',
			'Champawat29',
      'Bhubaneshwar21',
			'Dehradun29',
			'Haridwar29',
			'Nainital29',
			'Pauri Garhwal29',
			'Pithoragarh29',
			'Rudraprayag29',
			'Tehri Garhwal29',
			'Udham Singh Nagar29',
			'Uttarkashi29',
      'Baksa02',
			'Barpeta02',
			'Bongaigaon02',
			'Cachar02',
			'Chirang02',
			'Darrang02',
			'Dhemaji02',
			'Dima Hasao02',
			'Dhubri02',
			'Dibrugarh02',
			'Goalpara02',
			'Golaghat02',
			'Hailakandi02',
			'Jorhat02',
			'Kamrup02',
			'Kamrup Metropolitan02',
			'Karbi Anglong02',
			'Karimganj02',
			'Kokrajhar02',
			'Lakhimpur02',
			'Marigaon02',
			'Nagaon02',
			'Nalbari02',
			'Sibsagar02',
			'Sonitpur02',
			'Tinsukia02',
			'Udalguri02',			'Agra28',
			'Allahabad28',
			'Aligarh28',
			'Ambedkar Nagar28',
			'Auraiya28',
			'Azamgarh28',
			'Barabanki28',
      'Noida28',
			'Budaun28',
			'Bagpat28',
			'Bahraich28',
			'Bijnor28',
			'Ballia28',
			'Banda28',
			'Balrampur28',
			'Bareilly28',
			'Basti28',
			'Bulandshahr28',
			'Chandauli28',
			'Chhatrapati Shahuji Maharaj Nagar28',
			'Chitrakoot28',
			'Deoria28',
			'Etah28',
			'Kanshi Ram Nagar28',
			'Etawah28',
			'Firozabad28',
			'Farrukhabad28',
			'Fatehpur28',
			'Faizabad28',
			'Gautam Buddh Nagar28',
			'Gonda28',
			'Ghazipur28',
			'Gorakhpur28',
			'Ghaziabad28',
			'Hamirpur28',
			'Hardoi28',
			'Mahamaya Nagar28',
			'Jhansi28',
			'Jalaun28',
			'Jyotiba Phule Nagar28',
			'Jaunpur district28',
			'Ramabai Nagar (Kanpur Dehat)28',
			'Kannauj28',
			'Kanpur28',
			'Kaushambi28',
			'Kushinagar28',
			'Lalitpur28',
			'Lakhimpur Kheri28',
			'Lucknow28',
			'Mau28',
			'Meerut28',
			'Maharajganj28',
			'Mahoba28',
			'Mirzapur28',
			'Moradabad28',
			'Mainpuri28',
			'Mathura28',
			'Muzaffarnagar28',
			'Panchsheel Nagar district (Hapur)28',
			'Pilibhit28',
			'Shamli28',
			'Pratapgarh28',
			'Rampur28',
			'Raebareli28',
			'Saharanpur28',
			'Sitapur28',
			'Shahjahanpur28',
			'Sant Kabir Nagar28',
			'Siddharthnagar28',
			'Sonbhadra28',
			'Sant Ravidas Nagar28',
			'Sultanpur28',
			'Shravasti28',
			'Unnao28',
			'Varanasi28'
      'Araria03',
			'Arwal03',
			'Aurangabad03',
			'Banka03',
			'Begusarai03',
			'Bhagalpur03',
			'Bhojpur03',
			'Buxar03',
			'Darbhanga03',
			'East Champaran03',
			'Gaya03',
			'Gopalganj03',
			'Jamui03',
			'Jehanabad03',
			'Kaimur03',
			'Katihar03',
			'Khagaria03',
			'Kishanganj03',
			'Lakhisarai03',
			'Madhepura03',
			'Madhubani03',
			'Munger03',
			'Muzaffarpur03',
			'Nalanda03',
			'Nawada03',
			'Patna03',
			'Purnia03',
			'Rohtas03',
			'Saharsa03',
			'Samastipur03',
			'Saran03',
			'Sheikhpura03',
			'Sheohar03',
			'Sitamarhi03',
			'Siwan03',
			'Supaul03',
			'Vaishali03',
			'West Champaran03',
			'Chandigarh03','Dhalai27',
			'North Tripura27',
			'South Tripura27',
			'Khowai27',
			'West Tripura27','Ariyalur26',
			'Chennai26',
			'Coimbatore26',
			'Cuddalore26',
			'Dharmapuri26',
			'Dindigul26',
			'Erode26',
			'Kanchipuram26',
			'Kanyakumari26',
			'Karur26',
			'Madurai26',
			'Nagapattinam26',
			'Nilgiris26',
			'Namakkal26',
			'Perambalur26',
			'Pudukkottai26',
			'Ramanathapuram26',
			'Salem26',
			'Sivaganga26',
			'Tirupur26',
			'Tiruchirappalli26',
			'Theni26',
			'Tirunelveli26',
			'Thanjavur26',
			'Thoothukudi26',
			'Tiruvallur26',
			'Tiruvarur26',
			'Tiruvannamalai26',
			'Vellore26',
			'Viluppuram26',
			'Virudhunagar26',
      'Bastar04',
			'Bijapur04',
			'Bilaspur04',
			'Dantewada04',
			'Dhamtari04',
			'Durg04',
			'Jashpur04',
			'Janjgir-Champa04',
			'Korba04',
			'Koriya04',
			'Kanker04',
			'Kabirdham (Kawardha)04',
			'Mahasamund04',
			'Narayanpur04',
			'Raigarh04',
			'Rajnandgaon04',
			'Raipur04',
			'Surguja04',
      'Dadra and Nagar Haveli05','East Sikkim25',
			'North Sikkim25',
			'South Sikkim25',
			'West Sikkim25',
      'Daman06',
			'Diu06',
      'Central Delhi07',
			'East Delhi07',
			'New Delhi07',
			'North Delhi07',
			'North East Delhi07',
			'North West Delhi07',
			'South Delhi07',
			'South West Delhi07',
			'West Delhi07',
      'North Goa08',
			'South Goa08',
      'Alirajpur15',
			'Anuppur15',
			'Ashok Nagar15',
			'Balaghat15',
			'Barwani15',
			'Betul15',
			'Bhind15',
			'Bhopal15',
			'Burhanpur15',
			'Chhatarpur15',
			'Chhindwara15',
			'Damoh15',
			'Datia15',
			'Dewas15',
			'Dhar15',
			'Dindori15',
			'Guna15',
			'Gwalior15',
			'Harda15',
			'Hoshangabad15',
			'Indore15',
			'Jabalpur15',
			'Jhabua15',
			'Katni15',
			'Khandwa (East Nimar)15',
			'Khargone (West Nimar)15',
			'Mandla15',
			'Mandsaur15',
			'Morena15',
			'Narsinghpur15',
			'Neemuch15',
			'Panna15',
			'Rewa15',
			'Rajgarh15',
			'Ratlam15',
			'Raisen15',
			'Sagar15',
			'Satna15',
			'Sehore15',
			'Seoni15',
			'Shahdol15',
			'Shajapur15',
			'Sheopur15',
			'Shivpuri15',
			'Sidhi15',
			'Singrauli15',
			'Tikamgarh15',
			'Ujjain15',
			'Umaria15',
			'Vidisha15','Ahmednagar16',
			'Akola16',
			'Amravati16',
			'Aurangabad16',
			'Bhandara16',
			'Beed16',
			'Buldhana16',
			'Chandrapur16',
			'Dhule16',
			'Gadchiroli16',
			'Gondia16',
			'Hingoli16',
			'Jalgaon16',
			'Jalna16',
			'Kolhapur16',
			'Latur16',
			'Mumbai16',
			'Navi Mumbai16',
			'Nandurbar16',
			'Nanded16',
			'Nagpur16',
			'Nashik16',
			'Osmanabad16',
			'Parbhani16',
			'Pune16',
			'Raigad16',
			'Ratnagiri16',
			'Sindhudurg16',
			'Sangli16',
			'Solapur16',
			'Satara16',
			'Thane16',
			'Wardha16',
			'Washim16',
			'Yavatmal16',
      'Bishnupur17',
			'Churachandpur17',
			'Chandel17',
			'Imphal East17',
			'Senapati17',
			'Tamenglong17',
			'Thoubal17',
			'Ukhrul17',
			'Imphal West17',
       'East Garo Hills18',
			'East Khasi Hills18',
			'Jaintia Hills18',
			'Ri Bhoi18',
			'South Garo Hills18',
			'West Garo Hills18',
			'West Khasi Hills18',
       'Aizawl19',
			'Champhai19',
			'Kolasib19',
			'Lawngtlai19',
			'Lunglei19',
			'Mamit19',
			'Saiha19',
			'Serchhip19',
       'Dimapur20',
			'Kohima20',
			'Mokokchung20',
			'Mon20',
			'Phek20',
			'Tuensang20',
			'Wokha20',
			'Zunheboto20',
	'Angul21',
			'Boudh (Bauda)21',
			'Bhadrak21',
			'Balangir21',
			'Bargarh (Baragarh)21',
			'Balasore21',
			'Cuttack21',
			'Debagarh (Deogarh)21',
			'Dhenkanal21',
			'Ganjam21',
			'Gajapati21',
			'Jharsuguda21',
			'Jajpur21',
			'Jagatsinghpur21',
			'Khordha21',
			'Kendujhar (Keonjhar)21',
			'Kalahandi21',
			'Kandhamal21',
			'Koraput21',
			'Kendrapara21',
			'Malkangiri21',
			'Mayurbhanj21',
			'Nabarangpur21',
			'Nuapada21',
			'Nayagarh21',
			'Puri21',
			'Rayagada21',
			'Sambalpur21',
			'Subarnapur (Sonepur)21',
			'Sundergarh21',
	'Karaikal22',
			'Mahe22',
			'Pondicherry22',
			'Yanam22',
	'Amritsar23',
			'Barnala23',
			'Bathinda23',
			'Firozpur23',
			'Faridkot23',
			'Fatehgarh Sahib23',
			'Fazilka23',
			'Gurdaspur23',
			'Hoshiarpur23',
			'Jalandhar23',
			'Kapurthala23',
			'Ludhiana23',
			'Mansa23',
			'Moga23',
			'Sri Muktsar Sahib23',
			'Pathankot23',
			'Patiala23',
			'Rupnagar23',
			'Ajitgarh (Mohali)23',
			'Sangrur23',
			'Nawanshahr23',
			'Tarn Taran23',
      'Ajmer24',
			'Alwar24',
			'Bikaner24',
			'Barmer24',
			'Banswara24',
			'Bharatpur24',
			'Baran24',
			'Bundi24',
			'Bhilwara24',
			'Churu24',
			'Chittorgarh24',
			'Dausa24',
			'Dholpur24',
			'Dungapur24',
			'Ganganagar24',
			'Hanumangarh24',
			'Jhunjhunu24',
			'Jalore24',
			'Jodhpur24',
			'Jaipur24',
			'Jaisalmer24',
			'Jhalawar24',
			'Karauli24',
			'Kota24',
			'Nagaur24',
			'Pali24',
			'Pratapgarh24',
			'Rajsamand24',
			'Sikar24',
			'Sawai Madhopur24',
			'Sirohi24',
			'Tonk24',
			'Udaipur24',
      'Ahmedabad09',
			'Amreli district09',
			'Anand09',
			'Banaskantha09',
			'Bharuch09',
			'Bhavnagar09',
			'Dahod09',
			'The Dangs09',
			'Gandhinagar09',
			'Jamnagar09',
			'Junagadh09',
			'Kutch09',
			'Kheda09',
			'Mehsana09',
			'Narmada09',
			'Navsari09',
			'Patan09',
			'Panchmahal09',
			'Porbandar09',
			'Rajkot09',
			'Sabarkantha09',
			'Surendranagar09',
			'Surat09',
			'Vyara09',
			'Vadodara09',
			'Valsad09',
'Ambala10',
			'Bhiwani10',
			'Faridabad10',
			'Fatehabad10',
			'Gurgaon10',
			'Hissar10',
			'Jhajjar10',
			'Jind10',
			'Karnal10',
			'Kaithal10',
			'Kurukshetra10',
			'Mahendragarh10',
			'Mewat10',
			'Palwal10',
			'Panchkula10',
			'Panipat10',
			'Rewari10',
			'Rohtak10',
			'Sirsa10',
	'Sonipat10',
			'Yamuna Nagar10',
'Bilaspur11',
			'Chamba11',
			'Hamirpur11',
			'Kangra11',
			'Kinnaur11',
			'Kullu11',
			'Lahaul and Spiti11',
			'Mandi11',
			'Shimla11',
			'Sirmaur11',
			'Solan11',
			'Una11',
'Anantnag12',
			'Badgam12',
			'Bandipora12',
			'Baramulla12',
			'Doda12',
			'Ganderbal12',
			'Jammu12',
			'Kargil12',
			'Kathua12',
			'Kishtwar12',
			'Kupwara12',
			'Kulgam12',
			'Leh12',
			'Poonch12',
			'Pulwama12',
			'Rajauri12',
			'Ramban12',
			'Reasi12',
			'Samba12',
'Shopian12',
			'Srinagar12',
			'Udhampur12',
'Bokaro13',
			'Chatra13',
			'Deoghar13',
			'Dhanbad13',
			'Dumka13',
			'East Singhbhum13',
			'Garhwa13',
			'Giridih13',
			'Godda13',
			'Gumla13',
			'Hazaribag13',
			'Jamtara13',
			'Khunti13',
			'Koderma13',
			'Latehar13',
			'Lohardaga13',
			'Pakur13',
			'Palamu13',
			'Ramgarh13',
			'Ranchi13',
			'Sahibganj13',
'Seraikela Kharsawan13',
			'Simdega13',
			'West Singhbhum13',
'Bagalkot14',
			'Bangalore Rural14',
			'Bangalore Urban14',
			'Belgaum14',
			'Bellary14',
			'Bidar14',
			'Bijapur14',
			'Chamarajnagar14',
			'Chikkamagaluru14',
			'Chikkaballapur14',
			'Chitradurga14',
			'Davanagere14',
			'Dharwad14',
			'Dakshina Kannada14',
			'Gadag14',
			'Gulbarga14',
			'Hassan14',
			'Haveri district14',
			'Kodagu14',
			'Kolar14',
			'Koppal14',
			'Mandya14',
			'Mysore14',
			'Raichur14',
			'Shimoga14',
	'Tumkur14',
			'Udupi14',
			'Uttara Kannada14',
			'Ramanagara14',
			'Yadgir14','Alappuzha31',
			'Ernakulam31',
			'Idukki31',
			'Kannur31',
			'Kasaragod31',
			'Kollam31',
			'Kottayam31',
			'Kozhikode31',
			'Malappuram31',
			'Palakkad31',
			'Pathanamthitta31',
			'Thrissur31',
			'Thiruvananthapuram31',
			'Wayanad31'] 
#print(Cities)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
   
loaded_model = pickle.load(open("model_random_forest.sav", 'rb'))
#list6 = pd.DataFrame([[1,25,1,0,0,0,0,0]],columns=['Gender','Age','BMI1','BMI2','BMI3','Alcohol','Smoker','Disease'])
#result = loaded_model.predict(list6)
#print(list6)
#print(result)
#functions
def main():

    def insert():
        if(name_box.get()=="" or 
            age_box.get()=="" or
            gender_box.get()=="" or
            marry_box.get()=="" or
            height_box.get()=="" or
            weight_box.get()=="" or
            alco_box.get()=="" or
            smoke_box.get()=="" or
            product_box.get()=="" or
            State_box.get()=="" or
            city_box.get()=="" or
            salary_box.get()=="" or
            policy_amount_box.get()=="" or
            duration_box.get()==""
            ):
            
            tkinter.messagebox.showwarning("Warring","Fields can not be empty!")
            

    def Age():
        age=int(age_box.get())
        if (age<18):
                
            tkinter.messagebox.showwarning("Warning!","You should be above 18 to apply for any kind of Life insurance policy!")
        if age>18 and age<=30:
            age=25
        if age>30 and age<=45:
            age=35
        if age>45 and age<=60:
            age=50
        if age>60:
            age=65
        return age
    def gender():
        gen=gender_box.get()
        if gen=="Male":
          return 1
        if gen=="Female":
          return 0
        else:
            tkinter.messagebox.showwarning("Warning!","Invalid choice in gender!")
    def mari():
        mar = marry_box.get()
        if mar=="Married":
          return 1
        elif mar=="Unmarried":
          return 0
        else:
            tkinter.messagebox.showwarning("Warning!","Invalid choice in Martial status!")
    def Smoke():
        smoke=smoke_box.get()
        if smoke=="Yes":
            return 1
        elif smoke=="No":
            return 0
        else: 
            tkinter.messagebox.showwarning("Warning!","Invalid chooice in Do you smoke?")
    def alcoh():
        alco=alco_box.get()
        if alco=="Yes":
            return 1
        elif alco=="No":
            return 0
        else:
            tkinter.messagebox.showwarning("Warning!","Invalid choice in Do you consume any kinds of alcohol!")
    def BMI():
        h=float(height_box.get())
        w=float(weight_box.get())
        h=h/100
        int_bmi=w/h**2
        #print(int_bmi)
        if int_bmi > 30:      #Obese
            bmi1=0
            bmi2=1
            bmi3=0
            return bmi1,bmi2,bmi3
        if int_bmi < 18.5:    #Underweight
            bmi1=0
            bmi2=0
            bmi3=1
            return bmi1,bmi2,bmi3
        else:             #Healthy
            bmi1=1
            bmi2=0
            bmi3=0
            return bmi1,bmi2,bmi3
    def Disease():
        
        if disease==1:
            return 6
        elif disease == 2:
            return 7
        elif disease>2:
            return 8
        else:
            return 0
    def selected_item():
        count=0
        for i in lb1.curselection():
            lb1.get(i)
            count=count+1
        if count==1:
           return 6
        elif count==2:
           return 7
        elif count>2:
            count=8
        else:
            count=0
        return count
    def checkcity():
        aa=city_box.get()
        if aa in city_checklist:
            return 1
        else:
            return 0
  
    insert()
    age=Age()
    gen=gender()
    alco=alcoh()
    smoke=Smoke()
    cnt = selected_item()
    bmi1,bmi2,bmi3=BMI()
    citys=checkcity()
  
   # print(citys)
    #df = pd.read_csv("./data.csv")
    #for row in df:
     #   if not row[0]:
    list1 = pd.DataFrame([[str(gen),str(age),str(bmi1),str(bmi2),str(bmi3),str(alco),str(smoke),str(cnt),str(citys)]],columns=['Gender','Age','BMI1','BMI2','BMI3','Alcohol','Smoker','Disease','City'])
    #print(list1)
    #list1=df.append(list1)
    #list1.to_csv('data.csv',index=False)  
    result = loaded_model.predict(list1)
    #tkinter.messagebox.showinfo("Risk level!",result)
    summ= float(policy_amount_box.get())   #policy sum float
    year= float(duration_box.get())   #policy duration float
    month=year*12

    premium=summ/month
    if result==1:
        premium=premium-(premium/10)
        return result, premium
    if result==2:
        return result, premium
    if result==3:
        premium=premium+((premium/100)*10)
        return result, premium
    if result==4:
        premium=premium+((premium/100)*20)
        return result, premium
    if result==5:
        premium=premium+((premium/100)*30)
        return result, premium
    if result==6:
        premium=premium+((premium/100)*40)
        return result, premium
    if result==7:
        premium=premium+((premium/100)*50)
        return result, premium
    if result==8: 
        premium=premium+((premium/100)*60)
        return result, premium
def callback(input):
      
    if input.isdigit():
        return True
                          
    elif input is "":
        return True
  
    else:
        return False 
        
def newwindow():
    new_window= Toplevel(window)
    new_window.geometry("750x500+530+330")
    new_window.title("Risk level")
    #new_window.resizable(False,False)
    name=name_box.get()
    name=name.title()
    duration=int(duration_box.get())
    salary= float(salary_box.get())
    e,p= main()
    lbl=Label(new_window,text=str(name)+", your risk level is "+str(e)+" in the range of 1-8.",font="times 18 bold")
    #lbl.pack()
    lbl.place(relx=0.5, rely=0.1, anchor = 'center')
    
    p=int(p)
    #lb2=Label(new_window,text=str(p),font="times 20 bold")
    #lb2.place(relx=0.5, rely=0.5, anchor = 'center')
    if e<=4:
        lb2=Label(new_window,text="Congratulation your risk level is on the lower side!",font="times 15")
        lb2.place(relx=0.5, rely=0.3, anchor = 'center')
        if p<= salary:
            lb3=Label(new_window,text="Based on your risk level, Your policy premium is: Rs. "+str(p)+"/- per month and \n your policy duration is for "+str(duration)+" years which is affordable on your salary.",font="times 15")
            lb3.place(relx=0.5, rely=0.5, anchor = 'center')
        if p> salary:
            lb3=Label(new_window,text="Based on your risk level, Your policy premium is: Rs. "+str(p)+"/- per month and \n your policy duration is for "+str(duration)+" years but we regret to say that this is not affordable on your salary.",font="times 15")
            lb3.place(relx=0.5, rely=0.5, anchor = 'center')
    if e>4:
        lb2=Label(new_window,text="Unfortunately, your risk level is on the higher side!",font="times 15")
        lb2.place(relx=0.5, rely=0.3, anchor = 'center')
        if p< salary:
            lb3=Label(new_window,text="Based on your risk level, Your policy premium is: Rs. "+str(p)+"/- per month and \n your policy duration is for "+str(duration)+" years which is affordable on your salary.",font="times 15")
            lb3.place(relx=0.5, rely=0.5, anchor = 'center')
        if p> salary:
            lb3=Label(new_window,text="Based on your risk level, Your policy premium is: Rs. "+str(p)+"/- per month and \n your policy duration is for "+str(duration)+" years but we regret to say that this is not affordable on your salary.",font="times 15")
            lb3.place(relx=0.5, rely=0.5, anchor = 'center')
    lbx=Label(new_window,text="Risk level is obtained using Random Forest Algorithm",font="times 8 bold")
    lbx.place(relx=0.5, rely=0.95, anchor = 'center')
    #lb.pack()
def citystate(event):
    
    global new_dist
    new_dist=[]
    ss=State_box.get()
    ss=State[ss]
    #print(ss)
    #print(State[ss])
    for x in Cities:
        if ss in x:
            new_dist.append(x[0:-2])
    #print(new_dist)
    city_box['values']=new_dist
window = Tk()
combo= Combobox(window)
reg = window.register(callback)
window.geometry("750x470+530+330")
window.minsize(750,500)
window.maxsize(750,500)
window.title("Life Insurance Application")
lbl0 = tf.Label(window, text="Kindly fill your informations",font="times 15 bold").grid(row=0,column=1)
lbl10=Label(window, text="Name: ",justify=LEFT).grid(row=1,column=0)
Label(window, text="Age: ").grid(row=8,column=0)
Label(window, text="Gender: ").grid(row=15,column=0)
Label(window, text="Martial Status: ").grid(row=22,column=0)
Label(window, text="Height in cm: ").grid(row=29,column=0)
Label(window, text="Weight in Kg: ").grid(row=36,column=0)
Label(window, text="Do you consume any kind of alcohol?").grid(row=43,column=0)
Label(window, text="Do you Smoke? ").grid(row=56,column=0)
Label(window, text="Select the product type: ").grid(row=82,column=0)
#Label(window, text="City").grid(row=110,column=0)
Label(window, text="State").grid(row=86,column=0)
Label(window, text="City").grid(row=90,column=0)
Label(window, text="Monthly Salary").grid(row=95,column=0)
Label(window, text="Policy Amount (Minimum Amount 75000/-)").grid(row=100,column=0)
Label(window, text="Policy Duration(In years)").grid(row=105,column=0)
Label(window, text="Diseases that you have been contracted before:").grid(row=110,column=0)
Label(window, text="Select from the given list").grid(row=110,column=1)


State_box=ttk.Combobox(window,width=47,values=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","MadhyaPradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Pondicherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])
city_box=ttk.Combobox(window,width=47,values=new_dist)
name_box=Entry(window,width=50)
age_box=Entry(window,width=50)
age_box.config(validate="key",validatecommand=(reg,'%P'))
gender_box=ttk.Combobox(window,width=47,values=["Male","Female"])
marry_box=ttk.Combobox(window,width=47,values=["Married","Unmarried"])
height_box=Entry(window,width=50)
height_box.config(validate="key",validatecommand=(reg,'%P'))

weight_box=Entry(window,width=50)
weight_box.config(validate="key",validatecommand=(reg,'%P'))
alco_box=ttk.Combobox(window,width=47,values=["Yes","No"])
smoke_box=ttk.Combobox(window,width=47,values=["Yes","No"])
product_box=ttk.Combobox(window,width=47,values=["Term Life Insurance","Whole Life Insurance","Endowment Policy","Money Back Policy"])
lb1= Listbox(window, selectmode="multiple",width=50,height=6)
lb1.insert(1,"Heart Disease")
lb1.insert(2,"COVID-19")
lb1.insert(3,"Cancers")
lb1.insert(4,"Ashtama or any other respitory disease")
lb1.insert(5,"Diabetes")
lb1.insert(6,"Alzheimer")
lb1.insert(7,"Tuberculosis")
State_box.bind("<<ComboboxSelected>>",citystate)
salary_box=Entry(window,width=50)
salary_box.config(validate="key",validatecommand=(reg,'%P'))
policy_amount_box=Entry(window,width=50)
policy_amount_box.config(validate="key",validatecommand=(reg,'%P'))
duration_box=ttk.Combobox(window,width=47,values=["10","20","30","40","50","60","70","80","90","100"])
#city_box=Entry(window,width=50),
#lb2= Listbox(window,width=50,height=1)
#lb2.insert(END,*city_list)
#lb2.bind('<<ListboxSelect>>',fill)
#city_box.bind('<KeyRelease>',checkkey)
name_box.grid(row=1,column=1)
age_box.grid(row=8,column=1)
#age_box.bind("<Return>",age)
gender_box.grid(row=15,column=1)
marry_box.grid(row=22,column=1)
height_box.grid(row=29,column=1)
weight_box.grid(row=36,column=1)
alco_box.grid(row=43,column=1)
smoke_box.grid(row=56,column=1)
product_box.grid(row=82,column=1)
#city_box.grid(row=110,column=1)

#lb2.grid(row=120,column=1)
State_box.grid(row=86,column=1)
city_box.grid(row=90,column=1)
salary_box.grid(row=95,column=1)
policy_amount_box.grid(row=100,column=1)
duration_box.grid(row=105,column=1)
lb1.grid(row=111,column=1)

#submit button
submit=Button(text="Submit", command=lambda: [ main(),newwindow()]).grid(row=200,column=1)


window.mainloop()
