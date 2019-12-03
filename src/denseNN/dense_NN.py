import sys
import pandas as pd
import networkx as nx
import tensorflow as tf
import graph_function as gf
import tensorflow_hub as hub
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split

def remove_duplicates(x):
    return list(dict.fromkeys(x))


def evaluate(model, test_df, embed, sub_num):
	test_sentences = test_df["Original_Sentences"].values
	# Reduce logging output.
	tf.logging.set_verbosity(tf.logging.ERROR)

	with tf.Session() as session:
	    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
	    test_embeddings = session.run(embed(test_sentences))
	    print (test_embeddings.shape)


	test_loss, test_acc = model.evaluate(test_embeddings, test_df[sub_num].values)

	print('Test accuracy:', test_acc)
	print('Test accuracy:', test_acc)

	y_predict = model.predict(test_embeddings)
	#print(y_predict)

	index = 0

	correct = [0,0]  # TN, TP
	wrong = [0,0]   # FN, FP

	for zero_prop, one_prop in y_predict:
	    predicted = 0 if zero_prop > one_prop else 1
	    true = int((test_df[sub_num].values)[index])
	    if true == predicted :
	        correct[true] += 1
	    else:
	        wrong[predicted] += 1
	    index += 1

	print('| TN = {0} | FP = {1} | \n| FN = {2} | TP = {3} |'.format(correct[0], wrong[1], wrong[0], correct[1]))

	TN = correct[0]; TP = correct[1]; FN = wrong[0]; FP = wrong[1];
	try:
		precision = TP / (FP + TP)
		recall = TP / (FN + TP)
		print("precision = ", precision)
		print("recall = ", recall)

		if (precision + recall)==0 :
			f1_score = 'Null'
		f1_score = 2 * (precision * recall) / (precision + recall)
		print("F1_score = ", f1_score)

		result_pd = pd.DataFrame([[precision,recall,f1_score]])
		result_pd.to_csv("NN_result.csv", mode = 'a',header= False)
	except:
		result_pd = pd.DataFrame([['Divided','By','Zero']])
		result_pd.to_csv("NN_result.csv", mode = 'a', header = False)




def main():
	data = pd.read_csv("../../data/data.csv")
	data = data.dropna()
	data['Filename'] = (data['Category'].str.replace("-", "")).str.title() \
						+ data['Filename'].str.title()


	subs = gf.read_subgraphs()
	sub_num = sys.argv[1]
	num = int(sub_num)
	sub = subs[num]

	for i in data['Quesition_number'].values:
	    filename = data.loc[i]['Filename']
	    big_graph = nx.drawing.nx_pydot.read_dot("../../data/basic_blocks/dot/" + filename + "-CFG.dot")
	    data.loc[i, sub_num] = gf.is_subgraph(big_graph, sub)


	# shuffle data and split it as train and test
	train_df, test_df = train_test_split(data, test_size=0.2, shuffle=True)
	print("Size of data : {}" .format(data.shape))
	print("Size of train data : {}" .format(train_df.shape))
	print("Size of test data : {}" .format(test_df.shape))



	module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
	# Import the Universal Sentence Encoder's TF Hub module
	embed = hub.Module(module_url)

	# Compute a representation for each message, showing various lengths supported.
	train_sentences = train_df["Original_Sentences"].values

	# Reduce logging output.
	tf.logging.set_verbosity(tf.logging.ERROR)

	with tf.Session() as session:
	    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
	    train_embeddings = session.run(embed(train_sentences))
	    print (train_embeddings.shape)


	model = Sequential([Dense(512, input_shape=(512,)),
					    Activation('relu'),
					    Dense(128),
					    Dense(32),
					    Dense(2),
					    Activation('softmax'),
						])


	model = Sequential([Dense(512, input_shape=(512,)),
					    Activation('relu'),
					    Dense(128),
					    Dense(64),
					    Dense(32),
					    Dense(2),
					    Activation('softmax'),
						])



	model.compile(optimizer='adam',
            	  loss='sparse_categorical_crossentropy',
            	  metrics=['accuracy'])

	model.fit(train_embeddings, train_df[sub_num].values, epochs=100)

	evaluate(model, test_df, embed, sub_num)



if __name__== "__main__":
	main()
