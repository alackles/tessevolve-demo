from repparse import parameters
# Turn the line of descent file into a single string for the purposes of creating a "meshline"
# Format is val1, val2, [val3, val4]; val1, val2, val3, val4;
def export_edges(lodpath="lod.csv", edgepath="edges.csv"):
    edge_list = []
    with open(lodpath, "r") as lod_file:
        next(lod_file)
        for line in lod_file:
            edge_list.append(" ".join(x for x in line.split(",")[1:4])) # grab x0, x1, x2
    with open(edgepath, "w") as edge_file:
        edge_file.write(",".join(edge_list))

def main():

    params = parameters()

    for p in params:
        dirpath = p["path"]
        lodpath = dirpath + "lod.csv"
        edgepath = lodpath.replace("lod", "edge")
        export_edges(lodpath, edgepath)
        print(dirpath)

if __name__ == "__main__":
    main()