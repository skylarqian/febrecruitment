from django.core.management.base import BaseCommand
from fileloaderapp.models import UploadedFile
import os

class Command(BaseCommand):
    help = 'Cleans up database entries for files that no longer exist on the filesystem.'

    def handle(self, *args, **kwargs):
        uploaded_files = UploadedFile.objects.all()
        deleted_count = 0
        for file in uploaded_files:
            file_path = file.file.path
            if not os.path.exists(file_path):
                # File doesn't exist, delete the entry from the database
                self.stdout.write(f"Deleting missing file entry: {file_path}")
                file.delete()
                deleted_count += 1
        
        self.stdout.write(f"Deleted {deleted_count} missing file entries.")