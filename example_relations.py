import spacy
from spanbert import SpanBERT
from spacy_help_functions import get_entities, create_entity_pairs
    
raw_text = "Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004, with college roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes. Bill Gates stepped down as chairman of Microsoft in February 2014 and assumed a new post as technology adviser to support the newly appointed CEO Satya Nadella. "

# TODO: filter entities of interest based on target relation
entities_of_interest = ["Schools_Attended", "Work_For", "Live_In", "Top_Member_Employees]

# Load spacy model
nlp = spacy.load("en_core_web_lg")  

# Load pre-trained SpanBERT model
spanbert = SpanBERT("./pretrained_spanbert")  

# Apply spacy model to raw text (to split to sentences, tokenize, extract entities etc.)
doc = nlp(raw_text)  

for sentence in doc.sents:  
    print("\n\nProcessing entence: {}".format(sentence))
    print("Tokenized sentence: {}".format([token.text for token in sentence]))
    ents = get_entities(sentence, entities_of_interest)
    print("spaCy extracted entities: {}".format(ents))
    
    # create entity pairs
    candidate_pairs = []
    sentence_entity_pairs = create_entity_pairs(sentence, entities_of_interest)
    for ep in sentence_entity_pairs:
        # TODO: keep subject-object pairs of the right type for the target relation (e.g., Person:Organization for the "Work_For" relation)
        candidate_pairs.append({"tokens": ep[0], "subj": ep[1], "obj": ep[2]})  # e1=Subject, e2=Object
        candidate_pairs.append({"tokens": ep[0], "subj": ep[2], "obj": ep[1]})  # e1=Object, e2=Subject
    

    # Classify Relations for all Candidate Entity Pairs using SpanBERT
    candidate_pairs = [p for p in candidate_pairs if not p["subj"][1] in ["DATE", "LOCATION"]]  # ignore subject entities with date/location type
    print("Candidate entity pairs:")
    for p in candidate_pairs:
        print("Subject: {}\tObject: {}".format(p["subj"][0:2], p["obj"][0:2]))
    print("Applying SpanBERT for each of the {} candidate pairs. This should take some time...".format(len(candidate_pairs)))

    if len(candidate_pairs) == 0:
        continue
    
    relation_preds = spanbert.predict(candidate_pairs)  # get predictions: list of (relation, confidence) pairs

    # Print Extracted Relations
    print("\nExtracted relations:")
    for ex, pred in list(zip(candidate_pairs, relation_preds)):
        print("\tSubject: {}\tObject: {}\tRelation: {}\tConfidence: {:.2f}".format(ex["subj"][0], ex["obj"][0], pred[0], pred[1]))

        # TODO: focus on target relations
        # '1':"per:schools_attended"
        # '2':"per:employee_of"
        # '3':"per:cities_of_residence"
        # '4':"org:top_members"
SON_API_KEY, SEARCH_ENGINE_ID, r, t, q, k = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], \
                                                 sys.argv[6]
                        
#<r> is an integer between 1 and 4, indicating the relation to extract: 1 is for Schools_Attended, 2 is for Work_For, 3 is for Live_In, and 4 is for Top_Member_Employees
r_dict = {1: "Schools_Attended", 2: "Work_For", 3: "Live_In", 4: "Top_Member_Employees"}
                        
# Schools_Attended: Subject: PERSON, Object: ORGANIZATION
#Work_For: Subject: PERSON, Object: ORGANIZATION
#Live_In: Subject: PERSON, Object: one of LOCATION, CITY, STATE_OR_PROVINCE, or COUNTRY
#Top_Member_Employees: Subject: ORGANIZATION, Object: PERSON
                       
r_list = {1: ["PERSON", "ORGANIZATION"], 2: ["PERSON", "ORGANIZATION"], 3: ["PERSON", "LOCATION"],
              4: ["ORGANIZATION", "PERSON"]}
#initialize X for empty set 
X = {}
k = int(k)
t = float(t)
r = int(r)
print("API key= {}\nEngine key= {}\nRelation= {}\nThreshold= {}\nQuery= {}\number of Tuples= {}".format(JSON_API_KEY, SEARCH_ENGINE_ID, r_dict[r], t, q, k))
                        
urls = set()
queries = set()
not_k_results = True
iteration_counter = 1
                        
# while loop ends when top 10 results are satifisied 
while not_k_results:
    query_list = q.lower().strip('\n').split()
    for each_word in query_list:
        queries.add(each_word)
    url_list  = []
    new_query_url = search(q)
                        
    
    for i in new__query_url:
        if i not in urls:
            url_list.append(i)
            urls.add(i)
            
    print("=========== Iteration: {} - Query: {} ===========".format(iteration_counter, q))
  

    relations = []
    for key, value in sorted(X.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        if value < t:
            del X[key]
            
        else:
            relations.append([value, key[0], key[1]])
    print("Pruning relations below threshold..."\n"Number of tuples after pruning: {}".format(len(X))\n)
   

