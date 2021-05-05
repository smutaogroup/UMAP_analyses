#USAGE: This script works with lists of frame indices divided by clusters

def similarity(high, low):
    correct = 0
    
    # i and j are frame indices
    for i in low:
        i = int(i)
        
        for j in high:
            j = int(j)
            
            if i == j:
                correct += 1
                
    return correct


def iterate_clusters(reduced_list, high_list):
    reduced_sim = []
    best = []

    #Iterate over all the clusters in low dim
    for t in range(len(reduced_list)):
        best_sim = 0

        #Iterate over all the clusters in high dim
        for h in range(len(high_list)):

            # Check that high dimensional cluster has not been already assigned to other cluster. 
            if h not in best:
                sim = similarity(high_list[h], reduced_list[t]) # Calculate number of similar points

                # Check if similarity with current cluster is higher than highest similarity so far and then update
                if  sim > best_sim:
                    best_sim = sim
                    top = h

        # Append matching cluster and number of similar points to final list
        best.append(top)
        reduced_sim.append(best_sim) 
    return reduced_sim, best


def print_similarty_percentage(reduced_sim, n_points):
    tot = 0
    
    for y in reduced_sim:
        print('The number of similar points is: ' +str(y))
        tot += y
        print('The total number of similar points is (so far):' +str(tot))
    
    tot =(tot/n_points)*100
    print('The total number of similar points is (so far):' +str(tot))