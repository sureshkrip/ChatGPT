import boto3
import sagemaker

# Initialize the SageMaker session
sagemaker_session = sagemaker.Session()

# Create an Experiment
experiment = sagemaker_session.create_experiment(
    experiment_name="MyExperiment",
    description="My experiment description"
)

# Create a Trial
trial = sagemaker_session.create_trial(
    trial_name="MyTrial",
    experiment_name=experiment.experiment_name
)

# Create a Tracker
tracker = sagemaker.Tracker.create()

# Log metadata and metrics using the Tracker
with tracker.capture_aws_sdk_metrics():
    # Log metadata
    tracker.log_parameters({"learning_rate": 0.01, "batch_size": 128})
    tracker.log_input(name="train_data", media_type="s3/uri", value="s3://bucket/train_data.csv")
    
    # Run your training code
    # ...
    
    # Log metrics
    tracker.log_metric(name="accuracy", value=0.85)
    tracker.log_metric(name="loss", value=0.15)

# Attach the Tracker to the Trial
trial.add_trial_component(tracker.trial_component)

# Print the Trial and Experiment details
print(f"Trial: {trial.trial_name}")
print(f"Experiment: {experiment.experiment_name}")
