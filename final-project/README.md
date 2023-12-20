# Project - Create your own predictive model
# By Cat Markowska and Kelly Ocampo, P.3

Predictive models are used across industries to analyze and make predictions about data. From sports to beauty products to app usage, predictive models provide individuals and businesses with data to make informed decisions.

Throughout this module, you have learned how to program both supervised and unsupervised learning models. In this final project, you will create your own! Throughout this project, you will work through activities to complete the following steps: 

1. # Choose a dataset.
Our dataset is the abalone dataset on UC Irving's machine learning repository. 
Citation: Nash,Warwick, Sellers,Tracy, Talbot,Simon, Cawthorn,Andrew, and Ford,Wes. (1995). Abalone. UCI Machine Learning Repository. https://archive.ics.uci.edu/dataset/1/abalone

2. # Determine which algorithm is the best fit. Based on the dataset you choose, you will need to figure out which algorithm to use. This will require you to get to know your data and your goals! Is there a linear correlation between variables? Are you looking for numerical value or a label/category? Do you know the labels or do you need the model to create them for you?
We are using an unsupervised learning algorithm. There might not be a linear correlation between variables. We are looking for a label/category, but we do not know what labels we need. Thus, unsupervised learning is the best for our purpose. 

# - Do some tests with matplotlib and visualize your data.  Does it provide a good correlation?  Why or why not?
Our model did not work. However, looking at the data suggests that there is a correlation between the height and length of the abalone.

3. # Program your model. Once you have chosen your type of model, it’s time to create it! In this step, you will write a program that fits your chosen model to the data. Your program and output will be specific to the model you choose. 


4. # Analyze and present your findings. An important part of creating predictive models is being able to communicate the results. In this final step of the project, you will present your findings using slides or an infographic. Your product should include the following components:
- # Your reasoning for the algorithm you chose
- # An explanation and analysis of the output of your model: What results did your model produce? What do they mean?
- # A prediction based on your model
- # A summary of the accuracy of your model
- # Real world implications
We chose to use unsupervised learning because we wanted it to create clusters for us based on the abalone's weight and height. Our model ultimately did not end up working. We kept getting errors that we were unsure of how to fix. For instance, when we tried using the sex of the abalone as one instance of where data is getting pulled, it would not work. When we tried searching for te height, it only worked when we changed the capitalization of the word "height". In addition, some of our errors seemed to come from pandas and Anaconda itself. However, as stated above, looking at the data implies that longer abalone weigh more. This makes sense, as larger individuals are likely older and need to fill the space within their shells. The real-world implications of this could be used for abalone fising. Many species of abalone are already endangered. The correlation beween height and weight could be used to refine hunting practices; ie., abalone can only be harvested if it is between a certain height and weight to avoid overfishing specimens capable of reporduction, and to avoid picking up specimens who have not reached reproductive age. While this would make abalone cost more (there is a large demand for very little supply), it would also ensure the health of current abalone populations.