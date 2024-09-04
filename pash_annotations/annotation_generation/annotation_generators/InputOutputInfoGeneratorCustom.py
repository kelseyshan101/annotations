from pash_annotations.annotation_generation.annotation_generators.InputOutputInfoGenerator_Interface import InputOutputInfoGeneratorInterface

class InputOutputInfoGeneratorCustom(InputOutputInfoGeneratorInterface):
    def generate_info(self) -> None:
        self.set_first_operand_as_config_arg_type_string()
        if self.get_operand_list_length() == 1:
            self.set_implicit_use_of_stdin()
        else:
            self.all_but_first_operand_is_streaming_input()

        """
        if input_type == 'stdin':
            self.set_implicit_use_of_stdin()
        elif input_type == 'stream':
            self.all_operands_are_streaming_inputs()
        else:
            raise ValueError("Unsupported input type")

        if output_type == 'stdout':
            self.set_implicit_use_of_stdout()
        elif output_type == 'stream':
            self.all_operands_are_streaming_inputs()
        else:
            raise ValueError("Unsupported output type")
        """
        #When should set_all_operands_as_config_arg_type_string() be used
