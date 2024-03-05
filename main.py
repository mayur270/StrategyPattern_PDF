"""
This single page script defines operations related to PDF manipulation.

It includes abstract and concrete classes for performing various operations
on PDF files, such as merging multiple PDFs into a single file and splitting a
PDF into multiple files using Strategy design pattern.

Classes:
- PDFOperation: An abstract base class for defining PDF operations.
- MergeStrategy: A concrete implementation for merging PDF files.
- SplitStrategy: A concrete implementation for splitting PDF files.
- PDFEditor: A class for executing various PDF operations.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from pypdf import PdfReader, PdfWriter


class PDFOperation(ABC):
    """
    Abstract base class for PDF operations.

    Defines a common interface for operations like merging, splitting, or
    transforming PDF files.
    """

    @abstractmethod
    def execute(self, pdf_path: str, output_path: str) -> None:
        """
        Execute the PDF operation.

        This method should be implemented by concrete classes to perform
        a specific PDF operation, using the provided pdf_path and output_path.

        Args:
            pdf_path: The file path of the input PDF.
            output_path: The file path where output of operation is saved.
        """


class MergeStrategy(PDFOperation):
    """
    An operation for merging multiple PDF files into a single PDF file.

    This class implements the PDFOperation interface to provide a concrete
    strategy for merging PDFs.
    """

    def execute(self, pdf_paths: List[str], output_path: str) -> None:
        """
        Merge multiple PDF files into a single PDF file.

        Args:
            pdf_paths: A list of file paths for the PDFs to be merged.
            output_path: The file path where the merged PDF should be saved.
        """
        writer = PdfWriter()
        for path in pdf_paths:
            reader = PdfReader(path)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_path, 'wb') as out:
            writer.write(out)


class SplitStrategy(PDFOperation):
    """Split PDFs into separate pages."""

    def execute(
        self,
        pdf_path: str,
        output_path: str,
        start_page: int = 0,
        end_page: Optional[int] = None,
    ) -> None:
        """Split a PDF file into separate pages.

        Args:
            pdf_path: The path to the input PDF file.
            output_path: The path where the output PDF file should be saved.
            start_page: The starting page number for the split operation.
            end_page: The ending page number for the split operation
                (0-indexed). If None, splits until the last page.
        """
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        for page in reader.pages[start_page:end_page]:
            writer.add_page(page)
        with open(output_path, 'wb') as out:
            writer.write(out)


class PDFEditor(object):
    """A PDFEditor that allows executing different PDF operations.

    Attributes:
        _operation (PDFOperation): The current operation for PDF manipulation.
    """

    def __init__(self, operation: PDFOperation) -> None:
        """Initialize the PDFEditor with a specific PDF strategy.

        Args:
            operation (PDFOperation): A strategy object that defines the
                PDF operation to be executed, such as merging or splitting
                PDFs.
        """
        self._operation = operation

    @property
    def operation(self) -> PDFOperation:
        """Return the current strategy.

        Returns:
            The current PDFStrategy instance being used by the context.
        """
        return self._operation

    @operation.setter
    def operation(self, operation: PDFOperation) -> None:
        """Change to a new operation.

        Args:
            operation (PDFOperation): The PDF operation to be used for
                merge/split operations.
        """
        self._operation = operation

    def execute_operation(self, pdf_path: str, output_path: str) -> None:
        """Execute PDF operation using the specified strategy.

        Args:
            pdf_path: The file path of the input PDF.
            output_path: The file path where the output should be saved.
        """
        self._operation.execute(pdf_path, output_path)
