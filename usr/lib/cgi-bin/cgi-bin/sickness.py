# Gabriella Oye
import json;
import cgi;




def sickness(form_data):
    #threshold variables
    bacinfect = 0;
    virus = 0;
    symptom = 0;
    hosprec = 0;
    #mild general  symptoms
    if ("sneezing" in form_data and form_data["sneezing"]>0):
        symptom+=1;
    
    if ("coughing" in form_data and form_data["coughing"]>0):
        symptom+=1;
    
    if ("nausea" in form_data and form_data["nausea"]==1):
        symptom+=1;
    
    if ("fever" in form_data and form_data["fever"]>0):
        bacinfect+=1;
    
    if ("shakiness" in form_data and form_data["shakiness"]==1):
        symptom+=1;
    
    if ("fussiness" in form_data and form_data["fussiness"]>0):
        symptom+=1;
    

    #moderate general symptoms
    if ("shakiness" in form_data and form_data["shakiness"]==2):
        hosprec+=1;
    
    if ("vomiting" in form_data and form_data["vomiting"] == 1):
        symptom+=1;
    
    if ("nausea" in form_data and form_data["nausea"]==1):
        symptom+=1;
    
    #severe general symptoms
    if ("bloodpressure" in form_data and form_data["bloodpressure"] != 2):
        hosprec+=1;
    
    if ("nausea" in form_data and form_data["nausea"]==2):
        hosprec+=1;
    
    if ("hearrate" in form_data and form_data["heartrate"] != 2):
        hosprec+=1;
    



    #aches/pains
    if ("ha" in form_data):
        virus+=1;
        bacinfect+=1;
    
    if ("aa" in form_data):
        virus+=1;
        bacinfect+=1;
    
    if ("ca" in form_data):
        symptom+=1;
    
    if ("ta" in form_data):
        symptom+=1;
    
    if ("la" in form_data):
            hosprec+=1;
    
    if ("ea" in form_data):
        symptom+=1;
        
        
        
    #tightness
    if ("ht" in form_data):
        hosprec+=1;
    
    if ("at" in form_data):
        virus+=1;
        bacinfect+=1;
    
    if ("ct" in form_data):
        hosprec+=1;
    
    if ("tt" in form_data):
        hosprec+=1;
    
    if ("lt" in form_data):
        hosprec+=1;
    
    if ("et" in form_data):
        symptom+=1;
        
        
        
    #inflammation
    if ("hi" in form_data):
        hosprec+=1;
    
    if ("ai" in form_data):
        symptom+=1;
    
    if ("ci" in form_data):
        hosprec+=1;
    
    if ("ti" in form_data):
        hosprec+=1;
    
    if ("li" in form_data):
        hosprec+=1;
    
    if ("ei" in form_data):
        symptom+=1;
    



    #redness
    if ("hr" in form_data):
        symptom+=1;
    
    if ("ar" in form_data):
        symptom+=1;
    
    if ("cr" in form_data):
        symptom+=1;
    
    if ("tr" in form_data):
        virus+=1;
    
    if ("lr" in form_data):
        symptom+=1;
    
    if ("er" in form_data):
        symptom+=1;
    



    #soreness
    if ("hs" in form_data):
        symptom+=1;
    
    if ("a_s" in form_data):
        symptom+=1;
    
    if ("cs" in form_data):
        symptom+=1;
    
    if ("ts" in form_data):
        bacinfect+=1;
    
    if ("ls" in form_data):
        symptom+=1;
    
    if ("es" in form_data):
        symptom+=1;
    

    #bloating
    if ("hb" in form_data):
        hosprec+=1;
    
    if ("ab" in form_data):
        hosprec+=1;
    
    if ("cb" in form_data):
        hosprec+=1;
    
    if ("tb" in form_data):
        hosprec+=1;
    
    if ("lb" in form_data):
        hosprec+=1;
    
    if ("eb" in form_data):
        hosprec+=1;
    


    #congestion
    if ("hc" in form_data):
        symptom+=1;
    
    if ("ac" in form_data):
        bacinfect+=1;
    
    if ("c" in form_data):
        hosprec+=1;
    
    if ("tc" in form_data):
        symptom+=1;
    
    if ("lc" in form_data):
        virus+=1;
        bacinfect+=1;
    
    if ("ec" in form_data):
        symptom+=1;
    


    #sensitivitY
    if ("hy" in form_data):
        symptom+=1;
    
    if ("ay" in form_data):
        symptom+=1;
    
    if ("cy" in form_data):
        hosprec+=1;
    
    if ("ty" in form_data):
        symptom+=1;
    
    if ("ly" in form_data):
        virus+=1;
        bacinfect+=1;
    
    if ("ey" in form_data):
        symptom+=1;
    recomendations = {}
    recomendations["br"] = bacinfect
    recomendations["vr"] = virus
    recomendations["sr"] = symptom
    recomendations["hosr"] = hosprec
    
    
    return recomendations
