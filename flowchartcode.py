import random
from tabulate import tabulate
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["yes", "no"]:
            return user_input
        print("Invalid input. Please enter 'yes' or 'no'.")


print("Implant biocompatibility: testing based on the duration of contact and the type of tissue")
print("\nFirst step is determining the duration of contact the implant has with the body\n")
print("\nThe following questions and results are based on the Open access FDA documents that relate to the biocompatibility of medical devices\n")
print("\nAs well as the ISO 10993 series, those which were available to the public\n")
print("\nThe FDA documents provided the conditions of the duration of contact (less than 24 hours, between 24 hours and 30 days, and more than 30 days)\n")

chemical_tests = {
                    'extractables and leachables': [
                    'Gas Chromatography (GC)',
                    'Liquid Chromatography (LC)',
                    'Mass Spectrometry (MS)',
                    'Inductively Coupled Plasma Spectroscopy (ICP)',
                    'Fourier Transform Infrared Spectroscopy (FTIR)',
                    'Infrared Spectroscopy (IR)',
                    'Mass Spectrometry',
                    'Residual Solvents',
                    'Atomic Absorption Spectroscopy (AAS)',
                    'Inductively Coupled Plasma Spectroscopy (ICP)'
                    ],
                'Bulk Material Characterization': [
                    'Atomic Absorption Spectroscopy (AAS)',
                    'Inductively Coupled Plasma Spectroscopy (ICP)',
                    'Thermal Analysis',
                    'Infrared Spectroscopy Analysis for Identity and Estimation of Gross Composition (Reflectance Spectroscopy, Transmission Spectroscopy)'
                    ],
                'Surface Characterization': [
                    'IR Reflectance Spectroscopy',
                    'Scanning Electron Microscopy (SEM)'
                    ]
                    }

mechanical_tests = {
                'Tensile Test': 'Measures the behavior of materials under tensile load to determine its strength, stiffness, and ductility (stress, strain, yield deformation).',
                'Compression Test': 'Measures the behavior of materials under compressive load to determine its compressive strength, stiffness, and deformation.',
                'Torsion Test': 'Measures the behavior of materials under torsional load (angular) to determine its torsional strength, stiffness, and ductility.',
                'Fatigue Test': 'Measures the behavior of materials under cyclic load applied at different angles to determine its fatigue strength and fatigue life.',
                'Fracture Test': 'Measures the required energy that will cause an already cracked material to fully break.',
                'Hardness Test': 'Measures the ability of materials to resist indentation, scratching, or deformation. There are different hardness tests, such as Brinell, Rockwell, and Vickers, which use different methods to measure hardness.',
                'Impact Test': 'Measures the behavior of materials under sudden impact or shock load to determine their impact strength and toughness.',
                'Creep Test': 'Also known as stress-relaxation test, it provides an idea of the behavior of the material under a constant stress.',
                'Nondestructive Testing': 'A set of testing that provides an assessment of the material\'s mechanical property without damaging the original material properties.'
                }



#first question (less than 24 hours)
question_1 = "Is the implant in contact with the body for less than 24 hours?"
answer_1 = get_user_input(question_1)

if answer_1 == "yes":
    #q1=yes ( less than 24 hours)
    # Second question
    print("\nYou have answered yes to the first question, please answer the second question\n")
    question_2 = "Is the implant in contact with bone or tissue?"
    
    answer_2 = get_user_input(question_2)
    
    print("\nYou have answered", answer_2, "to the second question\n")
        #q1=yes, q2=yes (less than 24 hours and in contact with bone or tissue)) 
    if answer_2 == "yes":
        # Third question
        question_3 = "Is it an orthopedic or dental implant?"
        answer_3 = get_user_input(question_3)
        print("\nYou have answered", answer_3, "to the third question\n")
        if answer_3 == "yes":
            #q1=yes, q2=yes, q3=yes (less than 24 hours, in contact with bone or tissue, and orthopedic or dental implant)

            biological_tests = {
                'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                'Pyrogenicity': 'Measures the potential of the material to cause fever.'
                }
            chemical_table = []
            for test_category, tests in chemical_tests.items():
                    chemical_table.append([test_category, '\n'.join(tests)])

            mechanical_table = []
            for test_category, description in mechanical_tests.items():
                    mechanical_table.append([test_category, description])

            biological_table = []
            for test, description in biological_tests.items():
                    biological_table.append([test, description])

            print("\nChemical Tests:")
            print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

            print("\nMechanical Tests:")
            print(tabulate(mechanical_table, headers=['Test', 'Description'], tablefmt='grid'))

            print("\nBiological Tests:")
            print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
            
        else:
            
            #q1=yes, q2=yes, q3=no (less than 24 hours, in contact with bone or tissue, and not orthopedic or dental implant)
            biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.'
                 }
            chemical_table = []
            for test_category, tests in chemical_tests.items():
                 chemical_table.append([test_category, '\n'.join(tests)])

            biological_table = []
            for test, description in biological_tests.items():
                biological_table.append([test, description])

            print("\nChemical Tests:")
            print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

            print("\nBiological Tests:")
            print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
    else:
        #q1=yes, q2=no (less than 24 hours and not in contact with bone or tissue)
        
            biological_tests = {
                  ' Cytotoxicity': 'Measures the toxicity of the material to cells.',
                 'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                 ' Acute Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                  'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                  'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell',
                  'implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time',
                  'hemocompatibility': 'Measures the potential of the material to cause an adverse reaction to blood',
                  }
            chemical_table = []
            for test_category, tests in chemical_tests.items():
             chemical_table.append([test_category, '\n'.join(tests)])

            biological_table = []
            for test, description in biological_tests.items():
                biological_table.append([test, description])

            print("\nChemical Tests:")
            print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

            print("\nBiological Tests:")
            print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
else:
    #q1=no (more than 24 hours)
    # Fourth question
    question_4 = "Is the implant in contact for more than 24 hours but less than 30 days?"
    answer_4 = get_user_input(question_4)
    
    if answer_4 == "yes":
        # q4 = yes (more than 24 hours but less than 30 days)
        # Fifth question
        question_5 = "Is the implant in contact with bone or tissue?"
        answer_5 = get_user_input(question_5)
        
        if answer_5 == "yes":
            #q4=yes, q5=yes (more than 24 hours but less than 30 days and in contact with bone or tissue)
            # Sixth question
            question_6 = "Is it an orthopedic or dental implant?"
            answer_6 = get_user_input(question_6)
                        
            if answer_6 == "yes":
                #q4=yes, q5=yes, q6=yes (more than 24 hours but less than 30 days, in contact with bone or tissue, and orthopedic or dental implant)
                

                    biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Acute Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                    'Subchronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                    'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.'
                    }

                    chemical_table = []
                    for test_category, tests in chemical_tests.items():
                        chemical_table.append([test_category, '\n'.join(tests)])

                    mechanical_table = []
                    for test_category, description in mechanical_tests.items():
                        mechanical_table.append([test_category, description])

                    biological_table = []
                    for test, description in biological_tests.items():
                        biological_table.append([test, description])

                    print("\nChemical Tests:")
                    print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

                    print("\nMechanical Tests:")
                    print(tabulate(mechanical_table, headers=['Test', 'Description'], tablefmt='grid'))

                    print("\nBiological Tests:")
                    print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
                        
                        
            else:
                #q4=yes, q5=yes, q6=no (more than 24 hours but less than 30 days, in contact with bone or tissue, and not orthopedic or dental implant)

                biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                    'Subchronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                    'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    }

                chemical_table = []
                for test_category, tests in chemical_tests.items():
                    chemical_table.append([test_category, '\n'.join(tests)])

                biological_table = []
                for test, description in biological_tests.items():
                    biological_table.append([test, description])

                print("\nChemical Tests:")
                print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

                print("\nBiological Tests:")
                print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
        else:
            #q4=yes, q5=no (more than 24 hours but less than 30 days and not in contact with bone or tissue)
            
            biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                    'Subchronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                    'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Hemocompatibility': 'Measures the potential of the material to cause an adverse reaction to blood.'
                     }

            chemical_table = []
            for test_category, tests in chemical_tests.items():
                    chemical_table.append([test_category, '\n'.join(tests)])

            biological_table = []
            for test, description in biological_tests.items():
                    biological_table.append([test, description])

            print("\nChemical Tests:")
            print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

            print("\nBiological Tests:")
            print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
    else:
        #q4=no (more than 30 days)
        question_7 = "Is the implant in contact for more than 30 days?"
        answer_7 = get_user_input(question_7)

        if answer_7 == "yes":
            #q7=yes (more than 30 days)
            # Eighth question
            question_8 = "Is the implant in contact with bone or tissue?"
            answer_8 = get_user_input(question_8)
       

            if answer_8 == "yes":
                #q7=yes, q8=yes (more than 30 days and in contact with bone or tissue)
                # Ninth question
                question_9 = "Is it an orthopedic or dental implant?"
                answer_9 = get_user_input(question_9)
                if answer_9 == "yes":
                #q7=yes, q8=yes, q9=yes (more than 30 days, in contact with bone or tissue, and orthopedic or dental implant)
                
                
                    biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                    'Subchronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                    'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Hemocompatibility': 'Measures the potential of the material to cause an adverse reaction to blood.',
                    'Chronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a long period of time.',
                    'Caricinogenicity': 'Measures the potential of the material to cause cancer.',
                      }
                    chemical_table = []
                    for test_category, tests in chemical_tests.items():
                        chemical_table.append([test_category, '\n'.join(tests)])

                    mechanical_table = []
                    for test_category, description in mechanical_tests.items():
                        mechanical_table.append([test_category, description])

                    biological_table = []
                    for test, description in biological_tests.items():
                        biological_table.append([test, description])

                    print("\nChemical Tests:")
                    print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

                    print("\nMechanical Tests:")
                    print(tabulate(mechanical_table, headers=['Test', 'Description'], tablefmt='grid'))

                    print("\nBiological Tests:")
                    print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
                else:
                    #q7=yes, q8=yes, q9=no (more than 30 days, in contact with bone or tissue, and not orthopedic or dental implant)
                    biological_tests = {
                'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                'Subchronic Toxicity':'Measures the potential of the material to cause toxicity to the body over a period of time.',
                'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                'Hemocompatibility': 'Measures the potential of the material to cause an adverse reaction to blood.',
                'Chronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a long period of time.',
                'Caricinogenicity': 'Measures the potential of the material to cause cancer.',}
                chemical_table = []
                for test_category, tests in chemical_tests.items():
                    chemical_table.append([test_category, '\n'.join(tests)])

                biological_table = []
                for test, description in biological_tests.items():
                    biological_table.append([test, description])

                print("\nChemical Tests:")
                print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

                print("\nBiological Tests:")
                print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid')),
        
            else:
                #q7=yes, q8=no (more than 30 days and not in contact with bone or tissue)
                
                biological_tests = {
                    'Cytotoxicity': 'Measures the toxicity of the material to cells.',
                    'Sensitization': 'Measures the potential of the material to cause an allergic reaction.',
                    'Irritation or Intracutaneous Reactivity': 'Measures the potential of the material to cause irritation or inflammation.',
                    'Systemic Toxicity': 'Measures the potential of the material to cause toxicity to the body.',
                    'Pyrogenicity': 'Measures the potential of the material to cause fever.',
                    'Subchronic Toxicity':'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Genotoxicity': 'Measures the potential of the material to cause damage to the genetic information within a cell.',
                    'Implantation': 'Measures the potential of the material to cause toxicity to the body over a period of time.',
                    'Hemocompatibility': 'Measures the potential of the material to cause an adverse reaction to blood.',
                    'Chronic Toxicity': 'Measures the potential of the material to cause toxicity to the body over a long period of time.',
                    'Caricinogenicity': 'Measures the potential of the material to cause cancer.',
                   }
                chemical_table = []
                for test_category, tests in chemical_tests.items():
                    chemical_table.append([test_category, '\n'.join(tests)])

                biological_table = []
                for test, description in biological_tests.items():
                    biological_table.append([test, description])

                print("\nChemical Tests:")
                print(tabulate(chemical_table, headers=['Test Category', 'Tests'], tablefmt='grid'))

                print("\nBiological Tests:")
                print(tabulate(biological_table, headers=['Test', 'Description'], tablefmt='grid'))
            
        else:
            #q7=no (less than 30 days)
            if answer_7 == "no":
                print("insufficient information") 
            
    
print("this is only a suggested framework, please consult review articles and standards for more information")
input('press enter to exist')




                    


        


                




   
            


