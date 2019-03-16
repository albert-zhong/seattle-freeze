import streams
import analysis
import locations


def main():
    # streams.create_stream(locations.HAWAII, "/home/albert/workspace/seattle-freeze/data/hawaii.csv")
    print(analysis.get_means("/home/albert/workspace/seattle-freeze/data/hawaii.csv"))
    print(analysis.get_means("/home/albert/workspace/seattle-freeze/data/seattle.csv"))

if __name__ == "__main__":
    main()