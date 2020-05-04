folder = '04_May_2020_02_36_01';
epis_num = 0;

path = ['../results/' folder  '/figures'];
save_path = ['../results/' folder  '/video/'];


v = VideoWriter([save_path, 'epis', int2str(epis_num),'_anim']);
open(v)

S = dir(fullfile(path,['epis',int2str(epis_num),'_*.png'])); % pattern to match filenames.
for k = 1:numel(S)
    F = fullfile(path,S(k).name);
    I = imread(F);
    writeVideo(v,I)
end

close(v)