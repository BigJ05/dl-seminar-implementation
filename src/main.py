from amr_utility import get_seq_label_simple


if __name__ == "__main__":
    # Loading easy dataset
    ds = get_seq_label_simple("Staphylococcus_aureus_cefoxitin_pbp4")

    seq_train = [x[0] for x in ds["train"]]
    y_train = [x[1] for x in ds["train"]]

    seq_test = [x[0] for x in ds["test"]]
    y_test = [x[1] for x in ds["test"]]

    print(seq_train)
