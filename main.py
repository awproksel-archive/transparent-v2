import json

def main():
    
    with open('data/lego.json') as lego_file:
        lego_data = json.load(lego_file)
        
        collection_total_pieces = 0
        collection_unique_active_build_days = []

        for set in lego_data:
            collection_total_pieces += set['piece_count']

            for date in set['active_days']:
                if date not in collection_unique_active_build_days:
                    collection_unique_active_build_days.append(date)

        print("Total Piece Count: {}".format(collection_total_pieces))
        print("Active Build Days: {}".format(collection_unique_active_build_days))
        print("Total Days Active: {}".format(len(collection_unique_active_build_days)))
        print("Avg Pieces Per Active Day: {:.2f}".format(collection_total_pieces/len(collection_unique_active_build_days)))

if __name__ == '__main__':
    main()
