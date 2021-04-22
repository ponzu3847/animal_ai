import coremltools

coreml_model=coremltools.convert(
    'animal_cnn_aug.h5',input_names='image',image_input_names='image',
    output_names='Prediction',class_labels=['monkey','boar','crow'])

coreml_model.save('./animal_cnn_aug.mlmodel')