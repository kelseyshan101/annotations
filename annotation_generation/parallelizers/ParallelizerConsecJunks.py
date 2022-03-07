
from parallelizers.Parallelizer_Interface import ParallelizerInterface
from parallelizers.AggregatorConcatenate import AggregatorConcatenate


class ParallelizerConsecJunks(ParallelizerInterface):
    # for details on what the functions do, check comments in ParallelizerInterface

    @staticmethod
    def __name__():
        return f'ConsecJunks'

    @staticmethod
    def make_parallelizer_mapper_seq_aggregator_conc(seq):
        return ParallelizerConsecJunks(seq, AggregatorConcatenate())
