library(tidyverse)
library(jsonlite)
library(stringr)
library(xtable)
getwd()


path = "/Users/nathanschneider/classes/72COSC/CS72FinalProject/codenames/results/bot_results_combined.txt"
json_data <- stream_in(file(path))

data = json_data %>%
  mutate(codemaster = str_match(codemaster, "<class 'players.codemaster.([^'.]*)(?:.AI)*Codemaster'>")[,2]) %>%
  mutate(guesser = str_match(guesser, "<class 'players.guesser.([^'.]*)(?:.AI)*Guesser'>")[,2]) %>%
  select(codemaster, guesser, total_turns,R,B,C,A) %>%
  mutate(win = total_turns != 25)

codemasters = data$codemaster %>% unique()
guessers = data$guesser %>% unique()
codemaster_order = c("Human","gpt3_complex","gpt3","glove_05","w2v_05","w2vglove_05","wn_lin","random")
guesser_order =c("Human","gpt3","glove","w2v","w2vglove","fasttext","wn_path","wn_lch","wn_wup","random")



check_self = function(a,b){
  if (a %in% codemasters){
    cm = a
    g = b
  }
  else{
    cm = b
    g = a
  }
  switch(  
    cm,  
    "Human"= g == "Human",
    "random" = g == "random",
    "gpt3_complex" = g == "gpt3",
    "gpt3"= g == "gpt3",
    "glove_05"= g == "glove" | g == "w2vglove",
    "w2v_05"= g == "w2vglove" | g== "w2v",
    "w2vglove_05" = g == "w2vglove" | g== "w2v" | g == "glove",
    "wn_lin" = str_detect(g,'wn'),
    cm == g
  )

}

to_print = data %>%
  mutate(self = unlist(map2( codemaster, guesser, check_self ))) %>%
  filter(self) %>%
  group_by(guesser) %>%
  summarize(avg_turns=mean(total_turns),win_rate = mean(win),precision=mean((R/(R+B+C+A))),games_played=n()) %>%
  arrange(-win_rate) %>%
  select(guesser,avg_turns,win_rate,precision)

print(xtable(to_print, type = "latex"), file = "~/Downloads/filename2.tex")


data %>%
  mutate(self = unlist(map2( codemaster, guesser, check_self ))) %>%
  filter(self) %>%
  group_by(guesser) %>%
  summarize(mean(total_turns),win_rate = mean(win),precision=mean((R/(R+B+C+A))),games_played=n()) %>%
  arrange(-win_rate)


data

to_print = data %>%
  group_by(codemaster) %>%
  summarize(avg_turns=mean(total_turns),win_rate = mean(win),precision=mean((R/(R+B+C+A))),games_played=n()) %>%
  arrange(-win_rate) %>%
  select(codemaster,avg_turns,win_rate,precision)

print(xtable(to_print, type = "latex"), file = "~/Downloads/filename2.tex")


to_print = data %>%
  group_by(guesser) %>%
  summarize(avg_turns=mean(total_turns),win_rate = mean(win),precision=mean((R/(R+B+C+A))),games_played=n()) %>%
  mutate(guesser = factor(guesser,levels=guesser_order)) %>%
  arrange(-win_rate) %>%
  select(guesser,avg_turns,win_rate,precision)


print(xtable(to_print, type = "latex"), file = "~/Downloads/filename2.tex")


# Human codemaster
data %>%
  filter(codemaster == "Human") %>%
  group_by(guesser) %>%
  summarize(mean(total_turns),win = mean(win), accuracy=mean((R/(R+B+C+A))),n()) %>%
  arrange(-win)

# Human guesser
data %>%
  filter(guesser == "Human") %>%
  group_by(codemaster) %>%
  summarize(mean(total_turns),win = mean(win), accuracy=mean((R/(R+B+C+A))),n()) %>%
  arrange(-win)


data %>%
  group_by(codemaster, guesser) %>%
  count() %>%
  arrange(n) %>%
  print(n=50)


data %>%
  select(guesser) %>%
  unique() %>%
  mutate(guesser = factor(guesser,levels=guesser_order))




data %>%
  group_by(codemaster,guesser) %>%
  summarize(win = mean(total_turns))


data %>%
  filter(codemaster %in% codemaster_order & guesser %in% guesser_order) %>%
  group_by(codemaster,guesser) %>%
  summarize(win = mean(win)*100) %>%
  ggplot(aes(y=factor(codemaster,levels=rev(codemaster_order)),
             x=factor(guesser,levels=guesser_order),fill=win,
             label = paste0(round(win, digits = 0),"%"))) +
  geom_tile(color = "white",
            lwd = 1.5,
            linetype = 1) +
  geom_text(color = "white", size = 4)+
  coord_fixed() +
  labs(x="Guesser Agent",y='Codemaster Agent',
       fill="Win Rate") +
  scale_x_discrete(position = "top") +
  scale_fill_continuous(high = "#15c221", low = "#222222")



data %>%
  filter(codemaster %in% codemaster_order & guesser %in% guesser_order) %>%
  group_by(codemaster,guesser) %>%
  summarize(win = mean(total_turns)) %>%
  ggplot(aes(y=factor(codemaster,levels=rev(codemaster_order)),
             x=factor(guesser,levels=guesser_order),fill=win,
             label = paste0(round(win, digits = 1)))) +
  geom_tile(color = "white",
            lwd = 1.5,
            linetype = 1) +
  geom_text(color = "white", size = 4)+
  coord_fixed() +
  labs(x="Guesser Agent",y='Codemaster Agent',
       fill="Average Turns\n to finish \n(Loss = 25)") +
  scale_x_discrete(position = "top") +
  scale_fill_continuous(high = "#d42c02", low = "#147eba")

data

make_hist = function(column,agent) {
  if (column == "codemaster"){
    data %>%
      filter(codemaster == agent)%>%
      ggplot(aes(x=total_turns,fill=factor(guesser,levels=guesser_order))) +
      geom_histogram(bins=25) +
      theme_minimal() +
      labs(fill="Guesser",x="Turns to finish (Loss=25)",y="Number of games")
    
  }
  else{
    data %>%
      filter(guesser == agent)%>%
      ggplot(aes(x=total_turns,fill=factor(codemaster,levels=codemaster_order))) +
      geom_histogram(bins=25) +
      theme_minimal() +
      labs(fill="Guesser",x="Turns to finish (Loss=25)",y="Number of games",
           title=paste("Game performance distribution for",column,agent))
  }
}

make_hist("codemaster","glove_05")
  
make_hist("codemaster","w2v_05")

make_hist("guesser","fasttext")

  
  
  