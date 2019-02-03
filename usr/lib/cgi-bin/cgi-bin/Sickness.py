# Gabriella Oye
import json;
import cgi;
#threshold variables
bacinfect = 0;
virus = 0;
symptom = 0;
hosprec = 0;



def sickness(form_data):
    #mild general  symptoms
    if (form_data["sneezing"]>0):
        symptom+=1;
    
    if (form_data["coughing"]>0):
        symptom+=1;
    
    if (form_data["nausea"]==1):
        symptom+=1;
    
    if (form_data["fever"]>0):
        bacinfect+=1;
    
    if (form_data["shakiness"]==1):
        symptom+=1;
    
    if (form_data["fussiness"]>0):
        symptom+=1;
    

    #moderate general symptoms
    if (form_data["shakiness"]==2):
        hosprec+=1;
    
    if (form_data["vomiting"] == 1):
        symptom+=1;
    
    if (form_data["nausea"]==1):
        symptom+=1;
    
    #severe general symptoms
    if (form_data["bloodpressure"] != 2):
        hosprec+=1;
    
    if (form_data["nausea"]==2):
        hosprec+=1;
    
    if (form_data["heartrate"] != 2):
        hosprec+=1;
    



    #aches/pains
    if (form_data["ha"]):
        virus+=1;
        bacinfect+=1;
    
    if (form_data["aa"]):
        virus+=1;
        bacinfect+=1;
    
    if (form_data["ca"]):
        symptom+=1;
    
    if (form_data["ta"]):
        symptom+=1;
    
    if (form_data["la"]):
            hosprec+=1;
    
    if (form_data["ea"]):
        symptom+=1;
        
        
        
    #tightness
    if (form_data["ht"]):
        hosprec+=1;
    
    if (form_data["at"]):
        virus+=1;
        bacinfect+=1;
    
    if (form_data["ct"]):
        hosprec+=1;
    
    if (form_data["tt"]):
        hosprec+=1;
    
    if (form_data["lt"]):
        hosprec+=1;
    
    if (form_data["et"]):                          
        symptom+=1;
    	
        
        
    #inflammation
    if (form_data["hi"]):
        hosprec+=1;
    
    if (form_data["ai"]):
        symptom+=1;
    
    if (form_data["ci"]):
        hosprec+=1;
    
    if (form_data["ti"]):
        hosprec+=1;
    
    if (form_data["li"]):
        hosprec+=1;
    
    if (form_data["ei"]):
        symptom+=1;
    



    #redness
    if (form_data["hr"]):
        symptom+=1;
    
    if (form_data["ar"]):
        symptom+=1;
    
    if (form_data["cr"]):
        symptom+=1;
    
    if (form_data["tr"]):
        virus+=1;
    
    if (form_data["lr"]):
        symptom+=1;
    
    if (form_data["er"]):
        symptom+=1;
    



    #soreness
    if (form_data["hs"]):
        symptom+=1;
    
    if (form_data["a_s"]):
        symptom+=1;
    
    if (form_data["cs"]):
        symptom+=1;
    
    if (form_data["ts"]):
        bacinfect+=1;
    
    if (form_data["ls"]):
        symptom+=1;
    
    if (form_data["es"]):
        symptom+=1;
    

    #bloating
    if (form_data["hb"]):
        hosprec+=1;
    
    if (form_data["ab"]):
        hosprec+=1;
    
    if (form_data["cb"]):
        hosprec+=1;
    
    if (form_data["tb"]):
        hosprec+=1;
    
    if (form_data["lb"]):
        hosprec+=1;
    
    if (form_data["eb"]):
        hosprec+=1;
    


    #congestion
    if (form_data["hc"]):
        symptom+=1;
    
    if (form_data["ac"]):
        bacinfect+=1;
    
    if (form_data["c"]):
        hosprec+=1;
    
    if (form_data["tc"]):
        symptom+=1;
    
    if (form_data["lc"]):
        virus+=1;
        bacinfect+=1;
    
    if (form_data["ec"]):
        symptom+=1;
    


    #sensitivitY
    if (form_data["hy"]):
        symptom+=1;
    
    if (form_data["ay"]):
        symptom+=1;
    
    if (form_data["cy"]):
        hosprec+=1;
    
    if (form_data["ty"]):
        symptom+=1;
    
    if (form_data["ly"]):
        virus+=1;
        bacinfect+=1;
    
    if (form_data["ey"]):
        symptom+=1;
    
	recomendations = {
		"br": bacinfect,
		"vr": virus,
		"sr": symptom,
		"hosr": hosprec
	}	
	return recommendations
