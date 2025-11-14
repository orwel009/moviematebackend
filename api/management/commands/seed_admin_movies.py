from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import AdminMovie

SAMPLE = [
        {"title":"Mariner's Call","media_type":"movie","director":"A. Castillo","genre":"Adventure","platform":"Prime","total_episodes":None},
    {"title":"Scarlet Horizon","media_type":"tv","director":"M. Takahashi","genre":"Drama","platform":"Netflix","total_episodes":8},
    {"title":"The Vault Runner","media_type":"movie","director":"E. Sokolov","genre":"Thriller","platform":"HBO","total_episodes":None},
    {"title":"Fractured Earth","media_type":"tv","director":"J. Martins","genre":"Sci-Fi","platform":"Disney+","total_episodes":10},
    {"title":"Wildshore Harbor","media_type":"movie","director":"H. Bhat","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"Ironfall Legion","media_type":"tv","director":"T. Johansson","genre":"Action","platform":"Prime","total_episodes":12},
    {"title":"Sparrowtail","media_type":"movie","director":"C. Mendes","genre":"Drama","platform":"Hulu","total_episodes":None},
    {"title":"Ghostline District","media_type":"tv","director":"U. Fernandes","genre":"Thriller","platform":"HBO","total_episodes":6},
    {"title":"Autumn Skye","media_type":"movie","director":"D. Chan","genre":"Indie","platform":"IndieStream","total_episodes":None},
    {"title":"Starcrest Chronicles","media_type":"tv","director":"P. Grayson","genre":"Sci-Fi","platform":"Netflix","total_episodes":9},

    {"title":"Crimson Yard","media_type":"movie","director":"R. Malik","genre":"Mystery","platform":"Prime","total_episodes":None},
    {"title":"Hollowgate","media_type":"tv","director":"K. Dupont","genre":"Horror","platform":"Shudder","total_episodes":10},
    {"title":"Glass Orchard","media_type":"movie","director":"S. Patel","genre":"Romance","platform":"Disney+","total_episodes":None},
    {"title":"Mesa Frontier","media_type":"tv","director":"O. Mendes","genre":"Adventure","platform":"Netflix","total_episodes":7},
    {"title":"Sunset Paragraphs","media_type":"movie","director":"I. Moreno","genre":"Drama","platform":"Prime","total_episodes":None},
    {"title":"Voltronic Edge","media_type":"tv","director":"L. Carter","genre":"Sci-Fi","platform":"HBO","total_episodes":11},
    {"title":"Fogtown Memoirs","media_type":"movie","director":"A. Silva","genre":"Mystery","platform":"Netflix","total_episodes":None},
    {"title":"Nimbus Station","media_type":"tv","director":"T. Yamamoto","genre":"Sci-Fi","platform":"Hulu","total_episodes":9},
    {"title":"Orchid Valley","media_type":"movie","director":"V. Arora","genre":"Drama","platform":"IndieStream","total_episodes":None},
    {"title":"The Meridian Files","media_type":"tv","director":"C. Leblanc","genre":"Crime","platform":"Prime","total_episodes":8},

    {"title":"Shattered Reef","media_type":"movie","director":"G. Navarro","genre":"Thriller","platform":"Prime","total_episodes":None},
    {"title":"The Whisper Vault","media_type":"tv","director":"Z. Park","genre":"Mystery","platform":"Netflix","total_episodes":10},
    {"title":"Oceansong","media_type":"movie","director":"B. Holtz","genre":"Documentary","platform":"Curiosity","total_episodes":None},
    {"title":"The Golden Corridor","media_type":"tv","director":"F. Rubio","genre":"Drama","platform":"HBO","total_episodes":6},
    {"title":"Copper Ridge","media_type":"movie","director":"C. Nair","genre":"Adventure","platform":"Disney+","total_episodes":None},
    {"title":"Quiet District","media_type":"tv","director":"E. Laurent","genre":"Romance","platform":"Hulu","total_episodes":7},
    {"title":"Shadow Orchard","media_type":"movie","director":"P. Ivanov","genre":"Mystery","platform":"Prime","total_episodes":None},
    {"title":"Gravity Pulse","media_type":"tv","director":"R. Sethi","genre":"Sci-Fi","platform":"Netflix","total_episodes":12},
    {"title":"Bluewood Dreams","media_type":"movie","director":"H. Jensen","genre":"Family","platform":"Netflix","total_episodes":None},
    {"title":"Empire of Dunes","media_type":"tv","director":"T. Romero","genre":"Adventure","platform":"Prime","total_episodes":10},

    {"title":"Winterline","media_type":"movie","director":"J. Okada","genre":"Drama","platform":"Hulu","total_episodes":None},
    {"title":"Cobalt Verse","media_type":"tv","director":"L. Dimitri","genre":"Sci-Fi","platform":"HBO","total_episodes":8},
    {"title":"Burnished Hearts","media_type":"movie","director":"N. Sterling","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"City Under Neon","media_type":"tv","director":"V. Zhang","genre":"Crime","platform":"Prime","total_episodes":9},
    {"title":"Serenity Ashes","media_type":"movie","director":"A. García","genre":"Historical","platform":"Disney+","total_episodes":None},
    {"title":"Lonewatch Beacon","media_type":"tv","director":"H. Fischer","genre":"Thriller","platform":"HBO","total_episodes":7},
    {"title":"Misty Riverbend","media_type":"movie","director":"M. Isaac","genre":"Drama","platform":"IndieStream","total_episodes":None},
    {"title":"The Aurora Directive","media_type":"tv","director":"C. Nguyen","genre":"Sci-Fi","platform":"Hulu","total_episodes":10},
    {"title":"Year of the Sparrow","media_type":"movie","director":"S. Kohli","genre":"Adventure","platform":"Prime","total_episodes":None},
    {"title":"Hearts of Ironvale","media_type":"tv","director":"R. Dominguez","genre":"Fantasy","platform":"Netflix","total_episodes":11},
]

class Command(BaseCommand):
    help = "Seed AdminMovie table with sample entries (30)."

    def handle(self, *args, **options):
        created = 0
        for item in SAMPLE:
            title = item['title']
            # skip if exists
            obj, was_created = AdminMovie.objects.get_or_create(
                title=title,
                defaults={
                    'media_type': item.get('media_type', 'movie'),
                    'director': item.get('director'),
                    'genre': item.get('genre'),
                    'platform': item.get('platform'),
                    'total_episodes': item.get('total_episodes'),
                    'synopsis': item.get('synopsis', ''),
                    'poster_url': item.get('poster_url', ''),
                    'created_at': timezone.now(),
                    'updated_at': timezone.now(),
                }
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"AdminMovie seed completed: {created} created, {len(SAMPLE)-created} skipped (already existed)."))
