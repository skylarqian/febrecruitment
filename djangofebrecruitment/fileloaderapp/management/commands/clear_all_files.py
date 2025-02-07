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
            if os.path.exists(file_path):
                # Delete the physical file from the filesystem
                os.remove(file_path)  # Remove the file from the filesystem
                print(f"Deleted physical file: {file_path}")
            file.delete()
            deleted_count += 1
        
        self.stdout.write(f"Deleted {deleted_count} missing file entries.")

        uploaded_files = UploadedFile.objects.all()
        self.stdout.write(f"currently {len(uploaded_files)} files")