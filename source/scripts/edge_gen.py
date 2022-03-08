from decimal import Decimal

from repparse import parameters
# Turn the line of descent file into a single string for the purposes of creating a "meshline"
# Format is val1, val2, [val3, val4]; val1, val2, val3, val4;
def export_edges(lodpath="lod.csv", edgepath="edges.csv"):
    edge_list = []
    with open(lodpath, "r") as lod_file:
        next(lod_file)
        for line in lod_file:
            edge_list.append(" ".join(str(Decimal(x) * 10) for x in line.split(",")[1:-1])) # grab middle values, not fitness or ID
    with open(edgepath, "w") as edge_file:
        edge_file.write(",".join(edge_list))

def main():

    lodnames = ["lod_full.csv", "lod_hi.csv", "lod_md.csv", "lod_lo.csv"]

    params = parameters()

    for p in params:
        dirpath = p["path"]
        lodpaths = [dirpath + x for x in lodnames]

        for lod in lodpaths:
            edge = lod.replace("lod", "edge")
            export_edges(lod, edge)

        print(dirpath)

if __name__ == "__main__":
    main()