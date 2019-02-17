import streams
import locations

def main():
    streams.write_to_csv(locations.SEATTLE, "/home/albert/workspace/seattle-freeze/data/seattle.csv")

main()