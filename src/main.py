import argparse

from data_manager import download
from preprocesing import preprocesing_dataset
from svm import run_svm
from bert.bert import run_bert


def run_model(model_type: str, param_type: str, percentage: int) -> None:
    """
    Run the specified model with specified parameters.

    Args:
        model_type (str): Type of model (svm or bert).
        param_type (str): Type of parameters (default or best).
        percentage (int): Percentage of dataset to use.

    Returns:
        None
    """
    if model_type == "svm":
        if param_type == "default":
            print("Running SVM with default parameters...")
        elif param_type == "best":
            print("Running SVM with best parameters...")
        run_svm(model_type=param_type, percentage_dataset=percentage)
    elif model_type == "bert":
        if param_type == "default":
            print("Running BERT with default parameters...")
        elif param_type == "best":
            print("Running BERT with best parameters...")
        run_bert(model_type=param_type, percentage_dataset=percentage)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Text Classification")
    parser.add_argument(
        "-dd",
        "--download-data",
        type=str,
        help="If passed, the dataset for text classification will be downloaded.",
    )
    parser.add_argument(
        "-pp",
        "--pre-processing",
        type=str,
        help="If passed, run text processing and save the processed text.",
    )
    parser.add_argument(
        "--svm",
        choices=["default", "best", "custom"],
        nargs="*",
        help="Train SVM model. Options: 'default', 'best'. You can specify both.",
    )
    parser.add_argument(
        "--bert",
        choices=["default", "best"],
        nargs="*",
        help="Train BERT model. Options: 'default', 'best'. You can specify both.",
    )

    parser.add_argument(
        "-p",
        "--percentage",
        type=int,
        default=100,
        help="Specify the percentage of dataset to use to teach the model.",
    )

    args = parser.parse_args()
    if args.download_data:
        download(args.download_data)

    if args.pre_processing:
        preprocesing_dataset(args.pre_processing)

    if args.svm:
        for svm_option in args.svm:
            run_model(model_type="svm", param_type=svm_option, percentage=args.percentage)
    if args.bert:
        for svm_option in args.bert:
            run_model(model_type="bert", param_type=svm_option, percentage=args.percentage)


if __name__ == "__main__":
    main()
    print("Finish program")
